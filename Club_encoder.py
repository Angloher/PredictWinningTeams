import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import sys

class Club_encoder(torch.nn.Module):
    def __init__(self):
        super(Club_encoder,self).__init__()
        self.input_size=500
        self.hidden_size=500
        self.num_layers=10
        self.lstm = nn.LSTM(input_size=self.input_size,num_layers=self.num_layers, hidden_size=self.hidden_size) 
        self.hidden_state = (torch.rand((self.num_layers, 1, self.hidden_size),requires_grad=False),torch.rand((self.num_layers, 1, self.hidden_size),requires_grad=False))
        self.feature_vector = torch.rand(1,1,500)
    
    def forward(self, x):   
        output, self.hidden_state = self.lstm(x, (self.hidden_state))
        self.hidden_state[0].detach_()
        self.hidden_state[1].detach_()
        self.feature_vector=output.data
        return output



