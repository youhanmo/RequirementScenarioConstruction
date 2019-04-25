# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:23:17 2019

@author: Administrator
"""
from pyhanlp import *
import pandas as pd
import re
'''
path = 'data/traindata.xlsx'
lib = pd.read_excel(path, header=None, index=None).fillna(0)
CustomDictionary = JClass("com.hankcs.hanlp.dictionary.CustomDictionary")
CustomDictionary.add("本车",'n')  # 动态增加
word_compose = []
for sentence in lib[0]:
    finished_word_list = HanLP.segment(sentence)
    word_list = [str(i.word) for i in finished_word_list]
    word_cat_list = [str(i.nature) for i in finished_word_list]
    word_compose.append(word_cat_list)


answer = []
i = 0
for line in lib[4]:
    answer.append((word_compose[i],line))
    i = i+1
print(answer)
'''

path = 'data/traindata.xlsx'

def load_data(path):
    lib = pd.read_excel(path, header=None, index=None).fillna(0)
    #CustomDictionary = JClass("com.hankcs.hanlp.dictionary.CustomDictionary")
    #CustomDictionary.add("本车",'n')  # 动态增加
    #CustomDictionary.remove("本车")  # 动态增加
    #CustomDictionary.remove("米处")  # 动态增加
    word_compose = []
    word_cat_compose = []
    sen_list= []
    for sentence in lib[0]:
        #CRFnewSegment = HanLP.newSegment("crf")
        #CRFnewSegment.enableNumberQuantifierRecognize(True)
        StandardTokenizer = JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')
        #StandardTokenizer.SEGMENT.enableNumberQuantifierRecognize(False)
        
        finished_word_list = StandardTokenizer.segment(sentence)
        #finished_word_list = HanLP.segment(sentence)
        #finished_word_list = CRFnewSegment.seg(sentence)
        #print(finished_word_list)
        
        word_list = [str(i.word) for i in finished_word_list]
        word_cat_list = [str(i.nature) for i in finished_word_list]
        sen = ''
        for index in word_list:
            sen = sen + ' ' + index
        sen_list.append(sen.strip())
        word_compose.append(word_list)
        word_cat_compose.append(word_cat_list)
        
    answer=[]
    i = 0
    for line in lib[4]:
        if line == 1:
            answer.append([sen_list[i],1])
        else:
            answer.append([sen_list[i],0])
        i = i + 1
    #print(answer)
    #return answer,word_compose,word_cat_compose
    print('finish loading data')
    return answer
#a = load_data(path)
#print(a)
