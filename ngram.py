# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:14:26 2015

@author: Ardavan
"""
import json,nltk
from goose import Goose
import numpy.random as rnd

def ngram(words,n=3):
    res = []; temp = []
    for i in range(len(words)-n):
        for j in range(n):
            temp.append(words[i+j])
        res.append((words[i],words[i+1],words[i+2]))
    return res
        
##example with news2.txt
with open("news2.txt","rb") as f:
    data=json.loads(f.read())
f.close(); processed = []

for i in data['result']['docs']:
    try:
        url = i['source']['original']['url']
        g = Goose(); article = g.extract(url=url)
        processed.append([url,article.title,article.meta_description,article.cleaned_text])
    except:
        pass
    
s = ""; s2 = ""
for i in processed:
    s+= i[2]
    s2+= i[3]
    
s = nltk.word_tokenize(s)
s2 = nltk.word_tokenize(s2)
f = ""; f2 = ""
i = rnd.random_integers(1,len(s)-3);c=0
temp = ngram(s); temp2 = []
while len(f) < 140:
    i = rnd.random_integers(0,len(s)-3); temp2.append(temp[i])
    i = rnd.random_integers(0,len(s)-3)
    if nltk.pos_tag(nltk.word_tokenize(temp[i][0]))[0][1] != nltk.pos_tag(nltk.word_tokenize(temp2[0][-1]))[0][1]:
        f += " ".join(temp2[0]) + " " + " ".join(temp[i]) + " "
    temp2 = []
f = f[:-1]
temp = ngram(s2); temp2 = []
while len(f2) < 140:
    i = rnd.random_integers(0,len(s2)-3); temp2.append(temp[i])
    i = rnd.random_integers(0,len(s2)-3)
    print nltk.pos_tag(nltk.word_tokenize(temp[i][0])), nltk.pos_tag(nltk.word_tokenize(temp2[0][-1]))[0][1]
    if nltk.pos_tag(nltk.word_tokenize(temp[i][0]))[0][1] != nltk.pos_tag(nltk.word_tokenize(temp2[0][-1]))[0][1]:
        f2 += " ".join(temp2[0]) + " " + " ".join(temp[i]) + " "
    temp2 = []
f2 = f2[:-1]
    
print f
print f2

            
        
        



