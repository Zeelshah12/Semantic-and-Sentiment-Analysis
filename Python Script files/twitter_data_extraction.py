# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:55:31 2019

@author: Dell
"""
import re
import csv
import tweepy as tw
#from typing import Dict, List 
import datetime

#for cleaning data like removal of emojis, urls and special characters
def cleanData(inputString):
    inputString = inputString.encode('ascii', 'ignore').decode('ascii')  #for emojis
    inputString = re.sub(r'http\S+', '', inputString) # for urls
    inputString = re.sub('[^A-Za-z0-9\.\,\'"]+', ' ', inputString) # for special characters
    return inputString
    
def checkNull(value):
  return (value if value != "" else "Nan")

def convert_timestamp(date_object):
    if isinstance(date_object, (datetime.date, datetime.datetime)):
        return date_object.timestamp()
    
#credentials obtained from twitter developer account    
access_token="1187505744779907072-2DZ0iihzVvZvo7hRtYi9sUjFkHTWIY"
access_token_secret="vnhpN7AKO4UzPRTQQKgmw2zZAjMTb4ROzLjKaapxkVV1w"
consumer_key="Ou8fZbB7fi1fITlX3hkuEune5"
consumer_secret="0qjjefKW8FQNkgGrGK30A93AmGOGly2LWRnVVntL6kYtmzh6sT"

#xchecking authentication
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#keywords to be searched in extracted data
search_words = "Canada OR University OR Dalhousie University OR Halifax OR Canada Education" 
#finding tweets upto limit 3000
tweets = tw.Cursor(api.search, q=search_words).items(3000) 

#opening and writting into csv file 
with open('my_twitter_data.csv', mode='w') as my_file:
  twitter_writer = csv.writer(my_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  twitter_writer.writerow(['Tweet_Text', 'Location', 'Time', 'User', 'User_Location'])
  for tweet in tweets:
      print(tweet)
      twitter_writer.writerow([cleanData(tweet.text), (tweet.place.name if tweet.place is not None else "N/a"), tweet.created_at, cleanData(tweet.user.name), cleanData(checkNull(tweet.user.location))])

print("Done")