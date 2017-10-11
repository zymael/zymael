import os.path
from os import listdir, rename
INPUTPATH = 'cards'
inputfiles = [f for f in listdir(INPUTPATH) if os.path.isfile(os.path.join(INPUTPATH, f))]

for x in inputfiles:
    if x.startswith("cups") or x.startswith("disks") or x.startswith("swords") or x.startswith("wands") :
        newname = x.split("-")
        #print(str(newname[1][:-4])+" of "+str(newname[0])+".jpg")
        rename(os.path.join(INPUTPATH,str(x)), os.path.join(INPUTPATH,str(newname[1][:-4])+" of "+str(newname[0])+".jpg"))
