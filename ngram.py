# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:14:26 2015

@author: Ardavan
"""
import json,nltk
from goose import Goose
import numpy.random as rnd

gram = {'NN':["NN","CC","NNP","IN","VBZ","NNS",":",".",",","(",")","VB","PRP","PRP$","JJ"],
        "DT":["IN","NN","NNP",",","JJ","VBG","JJS","NNS"],
        'CC':["DT","NN","NNS","VBD","NNP","PRP$","VBN","PRP"],
        'IN':["DT","NNP","PRP","PRP$","RB"],
        "NNP":["RB","CC",",",":",".","CD","NN","NNP","TO","JJR","RBR","NNS","VBD"],
        "VBZ":["WRB","RB","IN","JJ","WRB"],
        "NNS":["NN","VBP","TO",",","CC",".","IN","VBD",":","NNP"],
        ":":["NN","NNP","NNS","VBZ"],
        ".":["JJR", "DT", "NN","PRP","PRP$"],
        ",":["NNP","WDT","PRP","PRP$","NN","VBG","NNS","DT","CD","VBP","VBZ"],
        "(":["NNP","WDT","PRP","PRP$","NN","VBG","NNS","DT","CD","VBP","VBZ"],
        ")":["IN","NN","JJR", "DT", "NN","PRP","PRP$"],
        "VB":["DT","NN","TO","NNP","RP","PRP","PRP$","IN"],
        "PRP":["VBD","JJ","VB"],
        "PRP$":["NN","NNS"],
        "JJ":["NN","NNP","NNS",",","CD","TO"],
        "CD":["IN","NN","NNS",",",":",".",")","RB"],
        "RB":["VBD","DT","CD","NNP","IN","TO","NN"],
        "#":["CD"],
        "JJR":["NNP","VB","TO"],
        "VBP":["RBR","NN","NNS",'PRP$'],
        "RBR":["CC","IN"],
        'VBD':["PRP","JJ","DT","VBG","."],
        "VBG":["NN","NNS","IN"],
        "TO":["VB","DT","$"],
        "$":["CD"],
        "VBN":["TO"],
        "WDT":[]}

def ngram(words,n=3):
    res = []
    for i in range(len(words)-n+1):
        temp = []
        for j in range(n):
            temp.append(words[i+j])
        res.append(temp)
    return res
    
def grammar(types):
    if types[1] in gram[types[0]]:
        return True
    else:
        return False

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
    
s = nltk.word_tokenize(s); k = nltk.pos_tag(s)
s2 = nltk.word_tokenize(s2); k2 = nltk.pos_tag(s2)

res = {}
for i in k:
    if not i[0] in res:
        res[i[0]] = i[1]

f = ""; f2 = ""; temp2 = []; temp = ngram(s)
i = rnd.random_integers(0,len(s)-3); temp2.append(temp[i])
while len(f) < 140:
    i = rnd.random_integers(0,len(s)-3)
    if grammar((res[temp2[0][-1]],res[temp[i][0]])):
        f += " ".join(temp2[0]) + " " + " ".join(temp[i]) + " "
        i = rnd.random_integers(0,len(s)-3); temp2=[]; temp2.append(temp[i])
f = f[:-1]

temp = ngram(s2); temp2 = []
i = rnd.random_integers(0,len(s2)-3); temp2.append(temp[i])
res = {}
for i in k2:
    if not i[0] in res:
        res[i[0]] = i[1]
        
for i in range(len(k2)-1):
    if not k2[i][1] in gram:
        gram[k2[i][1]] = []
    if not k2[i+1][1] in gram[k2[i][1]]:
        gram[k2[i][1]].append(k2[i+1][1])
        
while len(f2) < 140:
    i = rnd.random_integers(0,len(s2)-3)
    if grammar((res[temp2[0][-1]],res[temp[i][0]])):
        f2 += " ".join(temp2[0]) + " " + " ".join(temp[i]) + " "
        i = rnd.random_integers(0,len(s2)-3); temp2=[]; temp2.append(temp[i])

f2 = f2[:-1]
    
print f
print f2

            
        
        



