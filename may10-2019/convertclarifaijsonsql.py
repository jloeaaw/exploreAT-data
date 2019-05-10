from pprint import pprint
import json
import sys
import unicodedata
import time

import fileinput
import pandas as pd



language="en"
f2 = open('./list.csv')

lines = f2.readline()
while lines:
	fileis=lines
	fileis=fileis.replace('\n', '')
	docid=fileis.replace('.json', '')
	#print(fileis)
	with open(fileis,'r') as f:
		#print(f)
		data = json.load(f)
		cvoutputs = data["outputs"][0]["data"]["concepts"]
		cvlength=len(cvoutputs)
		for x in range(0,cvlength):
			try:
				name= str(cvoutputs[x]["name"]).decode('utf-8','ignore')
				score= cvoutputs[x]["value"]
				#print fileis, name, score
				selectis='insert into computervision (document_id,concept,score, language) values ('+ docid+',"'+ str(name)+'",'+ str(score)+',"'+language+'");'
				#print (name)
				print( selectis)
			except:
				print("error") 
	lines= f2.readline()

