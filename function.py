# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 22:04:37 2019

@author: Administrator
"""
import os
import codecs
import string
from nltk.corpus import stopwords
import snowballstemmer
import re
from itertools import chain
from gensim import models
import torch
from torch import nn
import torch.optim as optim
import torch.utils.data.dataloader as dataloader
from torch.autograd import Variable
import time
from sklearn.metrics import accuracy_score
from prepare import load_data  
from entity_detection import sen_split_CRF,get_entity,sen_split_NLP,sen_split_STD
from LSTMmodel import LSTM
from dict2rd5 import dict2rd5

def tokenizer(text):
    return [token.lower()  for token in text.split(' ')]

train_data = load_data('data/traindata.xlsx')
vocab_contains_repeat = []
train_token = []
for text,label in train_data:
    train_token.append(tokenizer(text))
    vocab_contains_repeat += tokenizer(text)


li = vocab_contains_repeat
vocab=list(set(li))
vocab.sort(key=li.index)
vocab_size = len(vocab)


#给每个词一个特定的编号
word_to_idx = {word:i+1 for i,word in enumerate(vocab)}
word_to_idx['<unk>'] = 0
# idx_to_word = {word_to_idx[k]:k for k,v in word_to_idx}
idx_to_word = {i+1: word for i, word in enumerate(vocab)}
idx_to_word[0] = '<unk>'
# print(idx_to_word)

def encode_samples(data,vocab):
    result = []
    for items in data:
        tmp = []
        for strs in items:
            if strs in word_to_idx:
                tmp.append(word_to_idx[strs])
            else:
                tmp.append(0)
        result.append(tmp)
    return result
#解决长度问题  所有文本的长度统一为max_length
def pad_samples(data,max_length = 10,PAD = 0):
    padded_features = []
    for item in data:
        if len(item) >= max_length:
            pad_item = item[:max_length]
        else:
            pad_item = item
            while(len(pad_item) < max_length):
                pad_item.append(PAD)
        padded_features.append(pad_item)
    return padded_features

def transform(inner):
    a = tokenizer(inner)
    #print(a)
    #print(vocab)
    b = [a]
    trainfeatures = torch.LongTensor(pad_samples(encode_samples(b,vocab)))
    #print(trainfeatures)
    trainfeatures = Variable(trainfeatures)
    return trainfeatures

def is_available_entity(innerlist):
    entitylist = ['树林','森林','房屋','加油站','商店','办公楼','超市','车站','地铁站','广告牌','标识','标志牌','标识牌','红绿灯','信号灯','桥','桥梁','高架桥','隧道','通道']
    is_valid_entity = True
    for word in innerlist:
        if word not in entitylist:
            is_valid_entity = False
    
    return is_valid_entity

def remove_unusable_entity(innerlist):
    entitylist = ['道路','公路','本车','车','高速路','树林','森林','房屋','加油站','商店','办公楼','超市','车站','地铁站','广告牌','标识','标志牌','标识牌','红绿灯','信号灯','桥','桥梁','高架桥','隧道','通道']
    
    for word in innerlist:
        if word not in entitylist:
            innerlist.remove(word)
    
    return innerlist
#为了保证模型构建词典一致，而且在之前的文件中有太多函数交杂，暂时不便于独立出新文件，所以重写了上述几个函数，以生成相同词典

sentences_file = open("data.txt","r")
sentences = sentences_file.read()
sentences_file.close()

net = torch.load('model\modelb3000lr0.005.pkl')
#sentences = u'''距树林后方55米左侧是本车，房屋位于道路前方18米左侧,红绿灯在本车前方111米处右侧，道路前方180米右侧是办公楼，车站在本车前方150米处左侧，道路前方66米左侧有一个加油站，树林在本车前方77米右侧，距广告牌后方171米右侧是公路，距标志牌后方171米左侧是公路，距标志牌后方199米右侧是道路'''
#sentences = u'''道路前方180米右侧是办公楼,红绿灯后方18米左侧是道路，红绿灯在本车前方111米处右侧'''
sentence_list = re.split('，|。|！|？|\r\n| |,|\ufeff|\n',sentences)
#分割句子
while '' in sentence_list:
    sentence_list.remove('')
    
#print(sentence_list)
dic_list = []
for inner in sentence_list:
    inner_entity,inner_direction,inner_number = get_entity(inner)
    inner_participle = sen_split_CRF(inner)
    #print(inner_participle)
    #inner='公路 在 房屋 的 前方 30 米 右侧'
    #print(inner_participle)
    for number in inner_number:
        if(not number.isnumeric()):
            inner_number.remove(number)
    inner_entity = remove_unusable_entity(inner_entity)
    if len(inner_entity)<2:
        EOE = 'can not execute this sentence: \n' + inner
        print(EOE)
        continue
    #print(inner_participle)
    #print(transform(inner_participle))
    dirr=''
    out = net(transform(inner_participle))
    #print(out)
    if out[0][0]>out[0][1] :
        #print('左侧')
        dirr='左侧'
    else:
        #print('右侧')
        dirr='右侧'
    #print(inner_number)
    length = 0
    #need_length = False
    
        
    if len(inner_number) == 2:
        length = inner_number[1]
    dic = { 'entity1':inner_entity[0],
           'entity2':inner_entity[1],
           'direction':dirr,
           'distance':inner_number[0],
           'length':length
         }
    
    
    if not (inner_entity[0] == '本车' or inner_entity[0] == '公路' or inner_entity[0] == '车' or inner_entity[0] == '道路' or inner_entity[0] == '高速公路' or inner_entity[0] == '高速路'):
        dic['entity1'] = inner_entity[1]
        dic['entity2'] = inner_entity[0]
        if dic['direction'] == '左侧':
            dic['direction'] = '右侧'
        elif dic['direction'] == '右侧':
            dic['direction'] = '左侧'
    #规范化dict 
    dic_list.append(dic)      
    
#print(dic_list)
dict2rd5(dic_list)
print('finishing generating data \nplease find data senario.rd5')
    

