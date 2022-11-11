#! /usr/bin/python
""" Creates database """

# Running this file will create an empty database

import sqlite3

# Create Database:

# open database
conn = sqlite3.connect('database.db')

# table includes columns for a username, email, and password
# all usernames must be unique
conn.execute('CREATE TABLE USERS (username TEXT, email TEXT, password TEXT, UNIQUE(username))')

# close database
conn.close()
