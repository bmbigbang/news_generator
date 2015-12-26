# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 12:33:57 2015

@author: Ardavan
"""

## more help with the api:
## https://alchemyapi.readme.io/v1.0/docs/rest-api-documentation
## https://alchemyapi.readme.io/v1.0/docs/full-list-of-supported-news-api-fields
import urllib2, json

key = "apikey=INSERT_KEY"

def news_Query(sentence=""):
    base="https://gateway-a.watsonplatform.net/calls/data/GetNews?"
    output = "&outputMode=json"
    time = "&start=now-12h&end=now"
    retu = "&return=original.url"
    if sentence:
        sentence = "&q.enriched.url.text=A[{0}]".format("^".join(sentence.split()))
    addressurl = base + key + output + time + retu + sentence
    req = urllib2.Request(addressurl)
    html = urllib2.urlopen(req).read().decode("utf-8")
    data = dict(json.loads(html))
    return data

#with open("news2.txt","wb") as f:
#    json.dump(news_Query(sentence="baseball game"),f)
#f.close()

##example with news1.txt
#with open("news1.txt","rb") as f:
#    data=json.loads(f.read())
#f.close()

#for i in data['result']['docs']:
#    for j in i['source']['enriched']['url']['keywords']:
#        print j;break

