# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 13:09:40 2019

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


class LSTM(nn.Module):
    def __init__(self,vocab_size,embed_size,num_hiddens,num_layers,bidirectional,weight,lables,use_gpu,**kwargs):

        super(LSTM,self).__init__(**kwargs)
        self.num_hiddens = num_hiddens
        self.num_layers = num_layers
        self.use_gpu = use_gpu
        self.bidirectional = bidirectional
        self.vocab_size=vocab_size
        self.embed_size=embed_size
        self.embedding = nn.Embedding.from_pretrained(weight)
        #self.embedding=torch.nn.Embedding(self.vocab_size,self.embed_size)
        self.embedding.weight.requires_grad = False
        self.encoder = nn.LSTM(input_size=embed_size,hidden_size=self.num_hiddens,
                               num_layers=num_layers,bidirectional=self.bidirectional
                               ,dropout=0)
        #bidirectional：True则为双向lstm默认为False
        if self.bidirectional:
            self.decoder = nn.Linear(num_hiddens*4,lables)
        else:
            self.decoder = nn.Linear(num_hiddens*2,lables)

    def forward(self, inputs):
        #size(64,500,300)
        embeddings = self.embedding(inputs)
        #permute后(500,64,300)   (batch,seq,input_size)
        #states.size(500,64,200)
        output, hidden = self.encoder(embeddings.permute([1, 0, 2]))
        #states[i] size(64,200)   -> encoding.size(64,400)
        encoding = torch.cat([output[0], output[-1]], dim=1)
        #这里就可以矩阵相乘了
        outputs = self.decoder(encoding)
        return outputs