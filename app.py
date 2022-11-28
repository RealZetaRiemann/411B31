"""Flask app for weatherspoons.com"""
from flask import Flask, render_template, url_for, redirect, session, request
from authlib.integrations.flask_client import OAuth
import secrets
import json
import sqlite3
import zipcodes
import time

app = Flask(__name__)

app.secret_key = secrets.token_bytes(32)

oauth = OAuth(app)

app.config['GITHUB_CLIENT_ID'] = "Enter key"
app.config['GITHUB_CLIENT_SECRET'] = "Enter key"

github = oauth.register (
  name = 'github',
    client_id = app.config["GITHUB_CLIENT_ID"],
    client_secret = app.config["GITHUB_CLIENT_SECRET"],
    access_token_url = 'https://github.com/login/oauth/access_token',
    access_token_params = None,
    authorize_url = 'https://github.com/login/oauth/authorize',
    authorize_params = None,
    api_base_url = 'https://api.github.com/',
    client_kwargs = {'scope': 'user:email'},
)

# Sign-in
@app.route('/')
def index():
  return render_template('index.html')

# Get zipcode from new users
@app.route('/newuser')
def newuser():
  failure = False
  return render_template('newuser.html', failure = failure)

# Home page from newuser form
@app.route('/home/', methods = ['POST', 'GET'])
def home():
  if request.method == 'GET':
    return render_template('home.html')
  if request.method == 'POST':

    # If the zipcode is real then render the home page normally
    zipcode = request.form.get("zipcode")
    if zipcodes.is_real(zipcode) == True:
      id = session["id"]

      # add zipcode to user profile in database
      conn = sqlite3.connect("database.db")
      cursor = conn.cursor()
      cursor.execute("UPDATE USERS SET zipcode = :zipcode WHERE id = :id", {'zipcode': zipcode, 'id': id})
      conn.commit()
      conn.close()

      # save zipcode during session for easy access
      session["zipcode"] = zipcode

      return render_template('home.html')

    # Otherwise return to the newuser page to try again
    else:
      failure = True
      return render_template('newuser.html', failure = failure)

# Get zipcode from new users
@app.route('/profile')
def profile():
  username = session["username"]
  realname = session["realname"]
  zipcode = session["zipcode"]
  return render_template('profile.html', username = username, realname = realname, zipcode = zipcode)

# Get zipcode from new users
@app.route('/favorites')
def favorites():
  return render_template('favorites.html')

# Github login
@app.route('/login/github')
def github_login():
    github = oauth.create_client('github')
    redirect_url = url_for('github_authorize', _external=True)
    return github.authorize_redirect(redirect_url)

# Github authorization
@app.route('/login/github/authorize')
def github_authorize():
    github = oauth.create_client('github')
    token = github.authorize_access_token()

    all_user_info = github.get('user').json()
    username = all_user_info['login']
    id = all_user_info['id']
    realname = all_user_info['name']

    # save user info during session (easier than using the database every time)
    session["username"] = username
    session["id"] = id
    session["realname"] = realname

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # add user's github id and username into the database 
    cursor.execute("INSERT OR IGNORE INTO USERS (id) VALUES (:id)", {'id': id})
    cursor.execute("UPDATE USERS SET username = :username WHERE id = :id", {'username': username, 'id': id})
    # if they have their real name on their github account, add that to the database as well
    if (realname != "None"):
      cursor.execute("UPDATE USERS SET realname = :realname WHERE id = :id", {'realname': realname, 'id': id})

    # check if the user's id has a zipcode attached
    zipcode = cursor.execute("SELECT zipcode FROM USERS WHERE id = (:id)", {'id': id})
    zipcode = cursor.fetchone()
    zipcode = zipcode[0]

    conn.commit()
    conn.close()

    # if this is a new account without a zipcode, then render a "newuser" html page which will ask them...
    # ...to input their zipcode before bringing them to the home page
    if zipcode == None:
      return render_template('newuser.html', username = username, id = id, realname = realname, zipcode = zipcode)

    # otherwise just go to the home page and save the zipcode during session for easy access
    session["zipcode"] = zipcode
    return render_template('home.html', username = username, id = id, realname = realname, zipcode = zipcode)

app.run(host='localhost', port=5000)
