import csv
import os.path
from os import listdir

INPUT = "./zymael/gematria.csv"

def make_dict_from_row(row):
    result = {}
    result['value'] = row[0]
    result['letter'] = row[1]
    return result

def makeValues():
    rawinput = []
    with open(INPUT,'r',encoding="utf8") as file:
    	reader = csv.reader(file)
    	for row in reader:
    		rawinput.append(row)
    values = []
    for x in rawinput:
    	   values.append(make_dict_from_row(x))
    valueDict = {}
    for x in values:
        valueDict[x['letter']]=x['value']

    return valueDict

def getValue(word):
    values=makeValues()
    value=0
    for letter in word:
        if letter in values:
            if letter=="א": #For some reason unable to cast 1 as an int, so this is a hacky workaround to ensure aleph is counted
                value+=1
            else:value+=int(values[letter])
            


    return value
