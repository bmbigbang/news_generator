# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 12:15:33 2015

@author: Ardavan
"""

## more help with the api:

from gensim.models import Word2Vec
from nltk.corpus import brown, movie_reviews, treebank
b = Word2Vec(brown.sents())
mr = Word2Vec(movie_reviews.sents())
t = Word2Vec(treebank.sents())

print b.most_similar('money',topn=5)
print mr.most_similar('money',topn=5)
print b.doesnt_match("money kt12 cheap")
#print b.n_similarity(['italian', 'shop'], ['japanese', 'restaurant'])
print b.most_similar(positive=['woman', 'king'], negative=['man'])
b.save_word2vec_format("matrix.txt", fvocab=None, binary=False)