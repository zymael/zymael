# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from .tarot import *
from .hga import *
from .gematria import *
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos

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
    return render_template("hga.html",output="null")

@app.route('/hgaresult',methods = ['POST'])
def hgaresult():
    if request.method == 'POST':
        result = request.form
        print(result)
        datelong = result['year']+"/"+result['month']+"/"+result['day']
        hour = result['hour']
        if result['ampm']=="PM": hour+=12
        time = hour+":"+result['minute']
        lat = result['latdegree']+result['lataxis']+result['latminute']
        lon = result['londegree']+result['lonaxis']+result['lonminute']
        DATE = Datetime(datelong, time, '+00:00')
        POS = GeoPos(lat, lon)
        aspects = Aspects(DATE,POS)
        zodiac = makeZodiac()
        signs = [[aspects.syzygy['sign'],str(aspects.syzygy['degree'])],[aspects.moon['sign'],str(aspects.moon['degree'])],[aspects.sun['sign'],str(aspects.sun['degree'])]]
        hebrew = makeName(zodiac, signs, 'hebrew')
        hebrewreverse = makeName(zodiac, signs, 'hebrewreverse')
        return render_template("hga.html",output=[hebrew,hebrewreverse])

@app.route('/gematria')
def gematria():
    return render_template('gematria.html',output="null")

@app.route('/gematriaresult',methods = ['POST'])
def gematriaresult():
    if request.method == 'POST':
        result = request.form
        print(result)
        word = result['input']
        value = getValue(word)
        return render_template("gematria.html",output=[word,value])
