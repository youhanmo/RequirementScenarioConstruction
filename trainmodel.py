# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 22:46:26 2019

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
torch.manual_seed(2)


def tokenizer(text):
    return [token.lower()  for token in text.split(' ')]

train_data = load_data('data/traindata.xlsx')
test_data = load_data('data/testdata.xlsx')

train_token = []
test_token = []

vocab_contains_repeat = []

for text,label in train_data:
    train_token.append(tokenizer(text))
    vocab_contains_repeat += tokenizer(text)
for text,label in test_data:
    test_token.append(tokenizer(text))
#print(train_token)
li = vocab_contains_repeat
vocab=list(set(li))
vocab.sort(key=li.index)
vocab_size = len(vocab)


filename = 'vec_trained/newsblogbbs.vec'
model = models.KeyedVectors.load_word2vec_format(filename,binary=False,encoding='utf-8')
  
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

train_features = torch.LongTensor(pad_samples(encode_samples(train_token,vocab))) #640*500
train_labels = torch.LongTensor([label for _,label in train_data])
#print(train_features)
test_features = torch.LongTensor(pad_samples(encode_samples(test_token,vocab)))
test_labels = torch.LongTensor([label for _,label in test_data])

#print('test_features:')
#print(test_features)

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
    
    
    
num_epochs = 5001
embed_size = 200
num_hiddens = 50
num_layers = 3
bidirectional = True
batch_size = 16
use_gpu = False
labels = 2
lr = 0.05

weight = torch.zeros(vocab_size+1,embed_size) #42*200

print(idx_to_word)

for i in range(len(model.index2word)):
    try:
        index = word_to_idx[model.index2word[i]]
    except:
        continue
    weight[index,:] = torch.from_numpy(model.get_vector(
        idx_to_word[word_to_idx[model.index2word[i]]]
    ))
#weight来自于word_emedding
print('finish transfering weight')
#print(idx_to_word)

net = LSTM(vocab_size=(vocab_size+1),embed_size=embed_size,num_hiddens=num_hiddens,num_layers=num_layers,
           bidirectional=bidirectional,weight=weight,
           lables=labels,use_gpu=use_gpu)
loss_function = nn.CrossEntropyLoss()
optimizer = optim.SGD(filter(lambda p:p.requires_grad,net.parameters()),lr=lr)


print('start contributing set')
train_set = torch.utils.data.TensorDataset(train_features,train_labels)
test_set = torch.utils.data.TensorDataset(test_features,test_labels)

train_iter = torch.utils.data.DataLoader(train_set,batch_size=batch_size,shuffle=True)
test_iter = torch.utils.data.DataLoader(test_set,batch_size=batch_size,shuffle=False)
print('get into training')
#print(train_iter)
f = open('testlr0.05.txt', 'w')
for epoch in range(num_epochs):
    if epoch%1000 == 0:
        print(epoch)
        newfilename = 'model\modelb'+str(epoch)+'lr0.005.pkl'
        torch.save(net, newfilename)
    start = time.time()
    train_loss,test_losses = 0,0
    train_acc,test_acc = 0,0
    n,m = 0,0
    
    for feature,label in train_iter:
        #print(feature)
        n += 1
        net.zero_grad()
        feature = Variable(feature)
        label = Variable(label)
        #print(label)
        #print('feature:')
        #print(feature)
        score = net(feature)
        #print('score:')
        #print(score)
        #print('label:')
        #print(label)
        loss = loss_function(score,label)
        loss.backward()
        optimizer.step()

        train_acc += accuracy_score(torch.argmax(score.cpu().data,dim=1),label.cpu())
        train_loss += loss

    with torch.no_grad():
        for test_feature,test_label in test_iter:
            m += 1
            test_feature = test_feature
            test_label = test_label
            #print('testlabel:'+str(test_label))
            test_score = net(test_feature)
            
            test_loss = loss_function(test_score,test_label)
            
            test_acc += accuracy_score(torch.argmax(test_score.cpu().data,dim=1),test_label.cpu())
            #print()
            #print('accuracyl:'+str(torch.argmax(test_score.cpu().data,dim=1)))
            test_losses += test_loss

    end = time.time()
    runtime = end - start
    f.write(('epoch: %d, train loss: %.4f, train acc: %.2f, test loss: %.4f, test acc: %.2f, time: %.2f \n  ' %
          (epoch, train_loss.data / n, train_acc / n, test_losses.data / m, test_acc / m, runtime)))
    print('epoch: %d, train loss: %.4f, train acc: %.2f, test loss: %.4f, test acc: %.2f, time: %.2f' %
          (epoch, train_loss.data / n, train_acc / n, test_losses.data / m, test_acc / m, runtime))
    
print('epoch: %d, train loss: %.4f, train acc: %.2f, test loss: %.4f, test acc: %.2f, time: %.2f' %
          (epoch, train_loss.data / n, train_acc / n, test_losses.data / m, test_acc / m, runtime))
#state = {'net':model.st, 'optimizer':optimizer.state_dict(), 'epoch':epoch}
#torch.save(state, dir)
f.close()
torch.save(net, 'model\modelb.pkl')
#inner='树林 在 本 车 的 前方 30 米 右侧'


def transform(inner):
    a = tokenizer(inner)
    #print(a)
    #print(vocab) 
    b = [a]
    trainfeatures = torch.LongTensor(pad_samples(encode_samples(b,vocab)))
    print(trainfeatures)
    trainfeatures = Variable(trainfeatures)
    return trainfeatures
    
    
#out = net(transform(inner))
#print(out)
