import os

from flask import Flask, render_template, flash, redirect, request, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

DBUSER = 'chicago'
DBPASS = '1q2w3e'
DBHOST = 'localhost'
DBPORT = '5432'
DBNAME = 'chicago_db'

app = Flask(__name__)

app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_pre_ping": True}
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'foobarbaz'

db = SQLAlchemy(app)