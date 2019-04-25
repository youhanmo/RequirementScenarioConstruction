# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 17:52:07 2019

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



def tokenizer(text):
    return [token.lower()  for token in text.split(' ')]

train_data = load_data('data/traindata.xlsx')
train_token = []
for text,label in train_data:
    train_token.append(tokenizer(text))


vocab = set(chain(*train_token))
vocab_size = len(vocab)


#给每个词一个特定的编号
word_to_idx = {word:i+1 for i,word in enumerate(vocab)}
word_to_idx['<unk>'] = 0
# idx_to_word = {word_to_idx[k]:k for k,v in word_to_idx}
idx_to_word = {i+1: word for i, word in enumerate(vocab)}
idx_to_word[0] = '<unk>'
#print(idx_to_word)

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


net = torch.load('model\modelb3000lr0.001.pkl')
print(net)
 
#inner='公路 在 房屋 的 前方 30 米 右侧'
inner = '距 本 车 前方 10 米 右侧 有 一个 标志牌'
print(inner)
print(transform(inner))
out = net(transform(inner))
if out[0][0]>out[0][1] :
    print('左侧')
else:
    print('右侧')
    
#print(out)