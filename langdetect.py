# -*- coding: utf-8 -*-
"""
Created on Wed Jan 06 13:56:45 2016

@author: ardavan
"""
import re
import unicodedata
import operator
import nltk

def ngram(words,n=1):
    res = []
    for i in range(len(words)-n+1):
        temp = []
        for j in range(n):
            temp.append(words[i+j])
        res.append(temp)
    return res

def checkletters(text):
    res = {}
    text = ngram(text.decode("utf-8"))
    for i in text:
        if i[0] not in res and not re.match(r'\s',i[0],flags=re.UNICODE):
            res[i[0]] = [unicodedata.name(i[0]),1]
        elif not re.match(r'\s',i[0],flags=re.UNICODE):
            res[i[0]][1] += 1
    mapping = {'russian':0 , 'chinese':0, 'latin':0}
    for i in res:
        if 'CJK' in res[i][0]:
            mapping['chinese'] += 1
        elif 'CYRILLIC' in res[i][0]:
            mapping['russian'] += 1
        elif 'LATIN' in res[i][0]:
            mapping['latin'] += 1
    return sorted(mapping.items(),key=operator.itemgetter(1),reverse=True)
    
def checklangs(text):
    text = ngram(text.decode("utf-8"),n=4)
    res={'english':[0, 'English-Latin1'],
         'german':[0, 'German_Deutsch-Latin1'],
         'italian':[0, 'Italian_Italiano-Latin1']}
    for x in res:
        cur = ngram(nltk.corpus.udhr.raw(res[x][1]),n=4)
        for y in cur:
            for z in text:
                if y == z:
                    res[x][0] += 1
    srtd = sorted(res.items(),key=operator.itemgetter(1),reverse=True)
    return [(x[0],x[1][0])for x in srtd]


text1 = "Попавший в снежную пробку оренбуржец"
print checkletters(text1)
text2 = "把百度设为主页把百度设为主页关于百度"
print checkletters(text2)
text3 = "this isn't english"
print checkletters(text3)
text4 = "dieses nicht Deutsch"
print checkletters(text4)

if checkletters(text3)[0][0] == 'latin':
    print checklangs(text3)
if checkletters(text4)[0][0] == 'latin':
    print checklangs(text4)