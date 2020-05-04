# -- coding: utf-8 --
"""
Created on Thu Nov 28 13:30:50 2019

@author: Dell
"""
import math,csv,re
canada_document = 0
halifax_document=0
university_document=0
total_documents=482

canada_eddoc=0
daluni_doc=0
arrayDoc = []

for j in range(482):
  canadaflg=0
  halifaxflg=0
  uniflg=0
  ceflg=0
  dalflg=0
  fileName = "final_newsapi_data_" +str(j) + ".txt"
  #print(fileName)
  with open(fileName,'r', encoding="utf-8") as f:
    content = (f.readline())
    #wordArray= re.split('" ", \n',content)
    #print(wordArray)
    #wordArray= re.split(r'\s{2,}', content)
    wordArray = content.split()
    #print(len(wordArray))
    #print(wordArray)    
    
    
    for i in range(len(wordArray)):
        
        if wordArray[i].lower()=='canada':
            canadaflg = canadaflg+1
            #print(fileName)
            
            #print(wordArray)
            
            #print("Article" + str(i) + " " + str(len(wordArray)))
            
        if wordArray[i].lower()=='halifax':
            halifaxflg = halifaxflg+1
            
        if wordArray[i].lower()=='university':
            uniflg = uniflg+1
        
        if((i+1)< len(wordArray) and wordArray[i].lower()=='canada'and wordArray[i+1].lower()=='education'):
            ceflg = ceflg+1
            
            
        if((i+1)< len(wordArray) and wordArray[i].lower()=='dalhousie'and wordArray[i+1].lower()=='university'):
            dalflg = dalflg+1
            
        #print(canadaflg)        

    if(canadaflg >0):
        canada_document = canada_document + 1
        print("Document Number " + str(j)+ "#total words "+str(len(wordArray)) +" canada words "+str(canadaflg))
        abc = str(j) +","+str(len(wordArray)) +","+str(canadaflg)
        arrayDoc.append(abc)
        
    
    if(halifaxflg >0):
        halifax_document = halifax_document + 1
        
    if(uniflg >0):
        university_document = university_document + 1   
        
    if(ceflg >0):
        canada_eddoc = canada_eddoc + 1 
        
    if(dalflg >0):
        daluni_doc = daluni_doc + 1 
        
term_canada=total_documents/canada_document
term_halifax=total_documents/halifax_document
term_university= total_documents/university_document
#term_canada_education=total_documents/canada_eddoc
term_dalhousie_university=total_documents/daluni_doc


print("Canada Document:" + str(canada_document))
#print(university_document)
#print(halifax_document)
#print(canada_eddoc)
#print(daluni_doc)
#print(math.log10(term_canada))
#print(math.log10(term_university))
#print(math.log10(term_halifax))
##print(term_canada_education)
#print(math.log10(term_dalhousie_university))
print(len(arrayDoc))

with open('Output_Semantic_analysis.csv','w') as output_semantic:
  writer = csv.writer(output_semantic)
  writer.writerow(['Total documents',total_documents])
  writer.writerow(['Search Query','Document Containing Term(df)','Total documents(N)/number of  documents  term  appeared (df)','Log10(N/df)'])
  writer.writerow(['Canada',canada_document, str(total_documents)+'/'+str(canada_document), str(round(math.log10(term_canada),2))])
  writer.writerow(['University',university_document, str(total_documents)+'/'+str(university_document), str(round(math.log10(term_university),2))])
  writer.writerow(['Halifax',halifax_document,str(total_documents)+'/'+str(halifax_document), str(round(math.log10(term_halifax),2))])
  writer.writerow(['Canada Education',canada_eddoc, 'NAN' , 'NAN'])
  writer.writerow(['Dalhousie University',daluni_doc,str(total_documents)+'/'+str(daluni_doc), str(round(math.log10(term_dalhousie_university),2))])


max=0
with open('Semantic_analysis_canada.csv','w') as output_semantic:
  writer = csv.writer(output_semantic)
  writer.writerow(['Term', 'Canada'])  
  writer.writerow(['Canada appeared in '+  str(len(arrayDoc)) + ' documents', 'Total words(m)', 'Frequency(f)'])
  for i in range(canada_document):
      string = arrayDoc[i].split(",")
      writer.writerow(["Article #"+ string[0], string[1], string[2]])
                       
      ratio= int(string[2])/int(string[1])                 
      print(round(ratio,2))
     
      if(ratio>max):
          max=ratio
          article = string[0]
print("max is "+str(round(max,2)))       
#print file  
fileName = "final_newsapi_data_" +str(article) + ".txt"
print(fileName)
with open(fileName,'r', encoding="utf-8") as f:
    content = (f.readline())
    print(content)
