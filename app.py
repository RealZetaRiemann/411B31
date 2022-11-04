"""Flask app for weatherspoons.com"""
import re
import secrets
from datetime import datetime
from flask import Flask, render_template, request, session, flash
import requests
from bs4 import BeautifulSoup
import sqlite3
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.secret_key = secrets.token_bytes(32)   # check for tampering

@app.route("/")
def index():
    """ Renders home page """
    return render_template('index.html')