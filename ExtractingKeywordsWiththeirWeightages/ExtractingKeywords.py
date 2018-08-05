import pandas as pd
import numpy as np
import PyPDF2
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import re
import os
os.chdir("F:\study")
filename ='JavaBasics-notes.pdf'

pdfFileObj = open(filename,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
num_pages = pdfReader.numPages
count = 0
text = ""

while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count += 1
    text += pageObj.extractText()
    if text != "":
        text = text
        tokens = word_tokenize(text)
        punctuations = ['(', ')', ';', ':', '[', ']', ',', ' ']
        stop_words = stopwords.words('english')
        keywords = []
        keywords = [word for word in tokens if not word in stop_words and not word  in string.punctuation]
        print(keywords)
        keywords = re.findall(r'[a-zA-Z]\w+', text)

len(keywords)

def weightage(word, text, number_of_documents=1):
    word_list = re.findall(word, text)
    number_of_times_word_appeared = len(word_list)
    tf = number_of_times_word_appeared / float(len(text))
    idf = np.log((number_of_documents) / float(number_of_times_word_appeared))
    tf_idf = tf * idf
    return number_of_times_word_appeared, tf, idf, tf_idf
df = pd.DataFrame(list(set(keywords)),columns=['keywords'])
df['number_of_times_word_appeared'] = df['keywords'].apply(lambda x: weightage(x,text)[0])
df['tf'] = df['keywords'].apply(lambda x: weightage(x,text)[1])
df['idf'] = df['keywords'].apply(lambda x: weightage(x,text)[2])
df['tf_idf'] = df['keywords'].apply(lambda x: weightage(x,text)[3])
df = df.sort_values('tf_idf',ascending=True)
df.to_csv('Keywords.csv')
df.head(20)













