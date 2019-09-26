import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from Match_encoder import Match_encoder
from Club_encoder import Club_encoder

class Model(torch.nn.Module):
    def __init__(self):
        super(Model,self).__init__()
        self.matchEncoder=Match_encoder()

    def forward(self,ClubEncoders):
        HomeTeam=ClubEncoders[0]
        AwayTeam=ClubEncoders[1]
        HomeInformation=HomeTeam.forward(AwayTeam.feature_vector)
        AwayInformation=AwayTeam.forward(HomeTeam.feature_vector)
        inp=torch.cat((HomeInformation,AwayInformation),2)
        return self.matchEncoder.forward(inp)