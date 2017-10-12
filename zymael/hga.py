import csv
import os.path
from os import listdir
from flatlib import const
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart

#import pdb; pdb.set_trace()


INPUT = "./zymael/zodiac.csv"

class Aspects():
    def __init__(self,DATE,POS):
        chart = Chart(DATE, POS)
        sun = chart.getObject(const.SUN)
        sunSign = sun.sign
        sunDegree = int(sun.signlon)
        moon = chart.getObject(const.MOON)
        moonSign = moon.sign
        moonDegree = int(moon.signlon)
        syzygy = chart.getObject(const.SYZYGY)
        syzygySign = syzygy.sign
        syzygyDegree = int(syzygy.signlon)

        self.sun={'sign':sunSign,'degree':sunDegree}
        self.moon={'sign':moonSign,'degree':moonDegree}
        self.syzygy={'sign':syzygySign,'degree':syzygyDegree}

def make_dict_from_row(row):
    result = {}
    result['sign'] = row[0]
    result['degree'] = row[1]
    result['hebrew'] = row[2]
    result['hebrewreverse'] = row[3]
    return result

def makeZodiac():
    rawinput = []
    with open(INPUT,'r',encoding="utf8") as file:
    	reader = csv.reader(file)
    	for row in reader:
    		rawinput.append(row)
    zodiac = []
    for x in rawinput:
    	   zodiac.append(make_dict_from_row(x))
    return zodiac

def getHebrew(zodiac,sign,degree):
    for x in zodiac:
        if x['sign']==sign:
            if x['degree']==degree:
                return x['hebrew']

def makeHebrewName(zodiac,signs):
    nameList = []
    for x in signs:
        nameList.append(getHebrew(zodiac,x[0],x[1]))
    hganame = "ל‎א‎"
    for x in nameList:
        hganame = hganame+x
    return hganame
