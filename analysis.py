#libraries
import sentifish
from sentifish import Sentiment
import pandas as pd
import numpy as np

from math import sin
from time import time

#source code
data_cleaning = []
analyzed_data = []

tiempo_inicial = time() 

print ('Reading data set...')
df = pd.read_csv("data/data-test.csv", sep=";", encoding='cp1252')

file = open("data/list_art_pron.txt","r",encoding="utf-8") 
text = file.read()
art_pron = text.split(",")

print ('Removing articles and pronouns...')
for row in df.message:
    for art in art_pron:
        row = row.replace(' ' +art+ ' ',' ')
        print(row)
    data_cleaning.append(row)

print ('Sentiment analysis...')
for data in data_cleaning:
    obj=Sentiment(data)
    polarity= obj.analyze()
    analyzed_data.append([data, polarity])

print('Saving data...')
res = pd.DataFrame(analyzed_data,
    columns = ["message","sentiment"]) 

print ('exporting data...')
res.to_csv (r'data\data-test-analyzed.csv', index = False, header=True)

tiempo_final = time() 
tiempo_ejecucion = tiempo_final - tiempo_inicial
print ('Run time: ',tiempo_ejecucion)