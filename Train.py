import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import time
from Model import Model
from Club_encoder import Club_encoder
from Create_data import Feature_extractor
from torch.autograd import Variable


def main():
    epochs=300
    Extractor=Feature_extractor()
    Extractor.process_data()
    stats=Extractor.playing_stats
    model=Model()
    optimizer = torch.optim.Adam(model.parameters(),lr=0.001,weight_decay=0.001)
    target_columns=['FTHG','FTAG']#,'HS','AS','HST','AST','HF','AF','HC','AC','HY','AY','HR','AR']
    criterion=nn.CrossEntropyLoss()
    for e in range(epochs):
        total_loss=0
        for country in stats:
            Encoders={}
            max_seasons=np.max([len(x) for x in country])
            s=0
            while s<max_seasons:
                for league in country:               
                    if len(league)-max_seasons<s:
                        season=league[s]
                        season_loss=0
                        start=time.time()
                        total_goals=0
                        for _,game in season.iterrows():
                            optimizer.zero_grad()
                            if game['HomeTeam'] not in Encoders.keys():
                                Encoders[game['HomeTeam']]=Club_encoder()
                            if game['AwayTeam'] not in Encoders.keys():
                                Encoders[game['AwayTeam']]=Club_encoder()
                            label=3*[0]
                            if target_columns[0]>target_columns[1]:
                                label=[[1,0,0]]
                            elif target_columns[0]<target_columns[1]:
                                label=[[0,1,0]]
                            else:
                                label=[[0,0,1]]
                            #total_goals+=np.sum(np.array(label))
                            labels = Variable(torch.from_numpy(np.array(label)))
                            result=model([Encoders[game['HomeTeam']],Encoders[game['AwayTeam']]])
                            loss=criterion(result,labels)
                            total_loss+=loss.data.item()
                            season_loss+=loss.data.item()    
                            loss.backward()
                            optimizer.step()
                        
                        print('in Season {} the avg loss was {} trained in {}s'.format(s,season_loss/len(league),time.time()-start))
                        print(labels)
                        print(result)
                        print('{} vs {} ended {} and was predicted {}\n'.format(game['HomeTeam'],game['AwayTeam'],labels[0],result[0][0]))
                s+=1
        print('in Epoch {} the loss was {}'.format(e,total_loss))
                        


def custom_loss(output,target):
    target=target.double()
    output=output.double()
    loss=output-target
    loss=torch.sum(torch.abs(loss))
    return loss

    

if __name__ == "__main__":
    main()