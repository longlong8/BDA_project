# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 01:21:41 2016

@author: jiheng
"""
import pandas as pd
import numpy as np
from sklearn.cross_validation import KFold
from sklearn.feature_extraction.text import CountVectorizer
from pyspark.mllib.tree import DecisionTree, DecisionTreeModel
from pyspark.mllib.util import MLUtils
data = pd.read_csv("Sentiment.csv")
test=pd.read_csv("geoTweets.csv")
text=test["text"]
location=test["place__full_name"]
traindata=data['SentimentText']
train=[]
label=[]
a=0
trainlabel=data['Sentiment']
for i in range(0,len(traindata)):
    try :
        
        temp=traindata[i].encode('utf-8')
        train.append(temp.lower())
        label.append(trainlabel[i])
    except:
        a=a+1
        

ngram_vectorizer = CountVectorizer(analyzer='word', ngram_range=(1, 1), min_df=1)
traindata = ngram_vectorizer.fit_transform(train)
model = DecisionTree.trainClassifier(traindata, numClasses=2, categoricalFeaturesInfo={},impurity='gini', maxDepth=5, maxBins=32)
testdata=[]
testlocation=[]

for i in range(0,len(text[i])-1):
    if type(text) is str:
        print i
        print text[i].lower()
        testdata.append(text[i].lower())
        testlocation.append(location[i])
        
testdata=ngram_vectorizer.transform(testdata)
predictions = model.predict(testdata.map(lambda x: x.features))
 
