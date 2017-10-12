import random

##CONFIG UP HERE##
DECKTYPE="thoth" #Valid entries are thoth or rider

def createDeck(type):
    deck =[]
    trumps = []
    face = []
    suits = []

    if type=="thoth":
            trumps = ["adjustment","aeon","art","chariot","death","devil","emperor","empress","fool","fortune","hanged","hermit","hierophant","lovers","magician","moon","passion","priestess","star","sun","tower","universe"]
            face = ["princess","prince","queen","knight"]
            suits = ["wands","swords","disks","cups"]

    elif type=="rider":
            trumps= ["justice","judgement","temperance","chariot","death","devil","emperor","empress","fool","fortune","hanged","hermit","hierophant","lovers","magician","moon","strength","priestess","star","sun","tower","world"]
            face = ["page","knight","queen","king"]
            suits = ["wands","swords","pentacles","cups"]

    for suit in suits:
        for y in range(1,15):
            if y == 1: deck.append("ace of " + suit)
            elif y == 11: deck.append(face[0] + " of " + suit)
            elif y == 12: deck.append(face[1] + " of " + suit)
            elif y == 13: deck.append(face[2] + " of " + suit)
            elif y == 14: deck.append(face[3]+ " of " + suit)
            else: deck.append(str(y) + " of " + suit)
    for trump in trumps: deck.append(trump)

    return deck

def shuffle(deck):
    random.shuffle(deck)
    return deck

def getCard(deck,amount):
    draw = []
    for x in range (0,amount):
        draw.append(deck[x])
    return draw
