# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from .tarot import *
from .hga import *

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tarot')
def tarot():
    deck = createDeck("thoth")
    deck = shuffle(deck)
    return render_template('tarot.html',card=getCard(deck,3))

@app.route('/hga')
def hga():
    DATE = Datetime('1989/06/17', '17:00', '+00:00')
    POS = GeoPos('38n32', '8w54')
    aspects = Aspects(DATE,POS)
    zodiac = makeZodiac()
    signs = [[aspects.syzygy['sign'],str(aspects.syzygy['degree'])],[aspects.moon['sign'],str(aspects.moon['degree'])],[aspects.sun['sign'],str(aspects.sun['degree'])]]
    for x in signs:print(x)
    hebrew = makeHebrewName(zodiac, signs)
    return render_template("hga.html",output=hebrew)
