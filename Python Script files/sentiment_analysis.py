# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 10:33:58 2019

@author: Dell
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 15:07:15 2019

@author: Dell
"""

import csv

with open('my_twitter_data_assign3.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

positive_words=[]
with open('positive-words.txt') as posword:
  positive_words = [pos.strip() for pos in posword.readlines()]

negative_words=[]
with open('negative-words.txt',encoding="ISO-8859-1") as negword:
  negative_words = [neg.strip() for  neg in negword.readlines()]
  
positive_word_count={}
negative_word_count={}


#print(data)
data_list=[]
for val in data:
  for text in val:
    #print(text)
    data_list.append(text)
print(data_list) 

list_dict = []
with open('Output_polarity1.csv','w') as output_polarity:
  writer = csv.writer(output_polarity)
  writer.writerow(['Tweet','Message','Match','Polarity'])
  for count in range(len(data_list)):
      Dict = {}
      text_tweet = data_list[count].split(" ")
      for word in range(len(text_tweet)):
        dict_key = text_tweet[word]
        dict_key = dict_key.lower()
        if dict_key in Dict.keys():
          Dict[dict_key] = Dict[dict_key] + 1
        else:
          Dict[dict_key] = 1
      
      list_dict.append(Dict)
      positive_count=0
      negative_count=0
      neutral=0
      polarity="neutral"
      list_match=""
      list_positive =""
      list_negative = ""
      for value in Dict.keys():
        if value in positive_words:
          
          positive_count=positive_count+1
          if value in positive_word_count:
            positive_word_count[value] += 1
          else:
            positive_word_count[value] = 1
          list_positive=list_positive + value +","
        if value in negative_words:
          negative_count=negative_count+1
          if value in negative_word_count:
            negative_word_count[value] += 1
          else:
            negative_word_count[value] = 1
          list_negative=list_negative + value +","
        else:
          neutral=neutral+1   
      if(positive_count>negative_count):
        polarity="positive"  
        list_match=list_positive
      elif(positive_count<negative_count):
        polarity="negative"  
        list_match=list_negative
      else:
         list_match="NONE," 
      writer.writerow([count,data_list[count],list_match[:-1],polarity]);   

      
  
      print(positive_count)
      print(negative_count)
      print(neutral)
      print(polarity)
      print(list_positive)
      print(list_negative)
print("Positive word list")      
print(positive_word_count)      
with open('Output_file_new.csv', 'w') as f:
    writer_new = csv.writer(f, lineterminator ='\n')
    writer_new.writerow(['Word','Frequency'])
    
    for key in positive_word_count.keys():
        writer_new.writerow([key,positive_word_count[key]])
        #f.write("%s,%s\n"%(key,positive_word_count[key]))
    for key in negative_word_count.keys():
        writer_new.writerow([key,negative_word_count[key]])
        #f.write("%s,%s\n"%(key,negative_word_count[key]))          
        
#print("Negative word list")        
#print(negative_word_count)      
#with open('negative.csv', 'w') as f:
   # for key in negative_word_count.keys():
    #    f.write("%s,%s\n"%(key,negative_word_count[key]))        

