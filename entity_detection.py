# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 22:14:45 2019

@author: Administrator
"""
from pyhanlp import *
import re


def get_result(arr):
    re_list = []
    dir_list = []
    num_list = []
    ner = ['n','ns','nz']
    dirr = ['f']
    nr = ['m']
    for x in arr:
        temp = x.split("/")
        if(temp[1] in ner):
            re_list.append(temp[0])
        if(temp[1] in dirr):
            dir_list.append(temp[0])
        if(temp[1] in nr):
            num_list.append(temp[0])
    return re_list,dir_list,num_list

'''
def get_entity(sentence):
    StandardTokenizer = JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')
    StandardTokenizer.SEGMENT.enableNumberQuantifierRecognize(True)
    StandardTokenizer.segment(sentence)
    CRFnewSegment = HanLP.newSegment("crf")
    CRFnewSegment.enableNumberQuantifierRecognize(True)
    CRFnewSegment.seg(sentence)
    print(sentence)
    sentence_list=re.split('，|。|！|？|\r\n| |,|\ufeff',sentence)
    while '' in sentence_list:
        sentence_list.remove('')
    for sen in sentence_list:
        analyzer = PerceptronLexicalAnalyzer()
        #segs = analyzer.analyze(sen)
        #print(segs)
        #arr = str(segs).split(" ")
        segs = StandardTokenizer.segment(sen)
        #print(StandardTokenizer.segment(sen))
        #arr = segs.split("，")
        newarr = []
        for i in range(segs.size()):
            segs[i] = str(segs[i])
            newarr.append(segs[i])
            #print(newarr)
        object_result,dir_result,num_result = get_result(newarr)
'''
def get_entity(sentence):
    
    #CustomDictionary = JClass("com.hankcs.hanlp.dictionary.CustomDictionary")
    #CustomDictionary.remove("米处")  # 动态增加
    #HanLP.Config.enableDebug()
    '''
    StandardTokenizer = JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')
    StandardTokenizer.SEGMENT.enableNumberQuantifierRecognize(True)
    StandardTokenizer.segment(sentence)
    '''
    #NLPTokenizer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
    #StandardTokenizer = JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')
    #StandardTokenizer.SEGMENT.enableNumberQuantifierRecognize(True)   
    StandardTokenizer = JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')
    #StandardTokenizer.SEGMENT.enableNumberQuantifierRecognize(True)
    StandardTokenizer.segment(sentence)
    CRFnewSegment = HanLP.newSegment("crf")
    #CRFnewSegment.enableNumberQuantifierRecognize(True)
    segs = CRFnewSegment.seg(sentence) 
    #analyzer = PerceptronLexicalAnalyzer()
    #segs = StandardTokenizer.segment(sentence)
    newarr = []
    for i in range(segs.size()):
        segs[i] = str(segs[i])
        newarr.append(segs[i])
    object_result,dir_result,num_result = get_result(newarr)
    
    return object_result,dir_result,num_result
    
def sen_split_CRF(sentence):
    CRFnewSegment = HanLP.newSegment("crf")
    segs = CRFnewSegment.seg(sentence)
    sen = ''
    print(segs)
    for word in segs:
        sen = sen+ ' ' + str(word)[0:str(word).find('/')]
    sen = sen.strip()
    
    return sen
    
def sen_split_NLP(sentence):
    NLPTokenizer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
    segs = NLPTokenizer.segment(sentence)
    #segs = CRFnewSegment.seg(sentence)
    sen = ''
    print(segs)
    for word in segs:
        sen = sen+ ' ' + str(word)[0:str(word).find('/')]
    sen = sen.strip()
    
    return sen

def sen_split_STD(sentence):
    StandardTokenizer = JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')
    segs = StandardTokenizer.segment(sentence)
    #segs = CRFnewSegment.seg(sentence)
    sen = ''
    print(segs)
    for word in segs:
        sen = sen+ ' ' + str(word)[0:str(word).find('/')]
    sen = sen.strip()
    
    return sen
#sentence=u'''在100米长的公路上，距原车前方50米右侧有一片树林，树林长10米，距本车前方九百九十九米左侧有一座房屋，距本车前方80米右侧有一广告牌。'''
#sentence=u'''距原车前方50米处右侧有一片树林'''   
#print(sen_split_CRF(sentence))
#print(get_entity(sentence))