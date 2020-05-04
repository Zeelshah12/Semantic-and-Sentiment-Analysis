# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:03:46 2019

@author: Dell
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 01:11:47 2019

@author: Dell
"""
import csv
import re
import requests

#cleaning data like removal of emoji,urls, special characters
def cleanData(inputString):
    inputString = inputString.encode('ascii', 'ignore').decode('ascii') # for emoji
    inputString = re.sub(r'http\S+', '', inputString) # for urls
    inputString = re.sub('[^A-Za-z0-9\.\,\'"]+', ' ', inputString) # for special characters
    return inputString

#key obtained from newsAPI account
key = 'bb75b658000349b2bd6aa0e743c6ee6d'
url = 'https://newsapi.org/v2/everything?'

keywords = ["Canada","University","Dalhousie University","Halifax","Canada Education"]

#opening and writing into csv file.
k=0
for keyword in keywords:
  parameters = {
    'q': keyword,
    'pageSize': 100,
    'apiKey': key
    }
  response = requests.get(url, params=parameters)
  # Convert the response to JSON format and pretty print it
  response_json = response.json()
  for i in response_json['articles']:
    filename= 'final_newsapi_data_' + str(k) + '.txt'
    with open(filename, mode='w+', encoding='UTF-8') as newsapidata:
      dataname = 'Title: ' + str(i['title']) + ' Content: ' + str(i['content']) + '  Description: ' + str(i['description'])
      newsapidata.write(cleanData(dataname))
    k=k+1