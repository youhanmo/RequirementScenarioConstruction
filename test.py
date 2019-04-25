# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 21:22:56 2019

@author: Administrator
"""

import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.optim as optim
a = torch.rand(3,3)
_,b = torch.max(a,1)
print(a)
print(b)
print(b.view(-1))

