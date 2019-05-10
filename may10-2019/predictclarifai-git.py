from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import unicodedata
import time
import json
import sys
import fileinput
import pandas as pd


dateprocessedis=str(pd.to_datetime('now'))
serviceis='clarifai'


app = ClarifaiApp(api_key='XX')
model = app.models.get('XX')

#filetoprocess. The file contains the documentid and image path
f = open('./processthis.csv')
# model to be used

line = f.readline()
while line:
    sp = []
    sp = line.split(';')
    docid=sp[0]
    nameis1=sp[1]
    print(docid)
    print(nameis1)
    nameis = str(nameis1)

    fileoutputname='./cvoutput/'+str(docid)+'.json'
   
    if (str(nameis1).find("%")) <0 : 
    	image = ClImage(url=nameis)
    	jsonData=model.predict([image])
    	time.sleep(2)
    	f1=open(fileoutputname, 'w+')
    	f1.write(str(jsonData))
    	f1.close()
    	time.sleep(2)
    else :
        print("Bad link")
    line= f.readline()
