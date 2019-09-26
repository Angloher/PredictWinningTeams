import torch.nn
import torch.nn.functional as F
import torch.optim as optim

class Match_encoder(torch.nn.Module):
    def __init__(self):
        super(Match_encoder,self).__init__()
        input_dim=1000
        Hidden_dim=500
        output_dim=2
        self.matcher=torch.nn.Sequential(
            torch.nn.Linear(input_dim,Hidden_dim),
            torch.nn.Linear(Hidden_dim,2*Hidden_dim),
            torch.nn.ReLU(),
            torch.nn.Linear(2*Hidden_dim,Hidden_dim),
            torch.nn.Linear(Hidden_dim,output_dim))#,
            #torch.nn.Sigmoid())
    
    def forward(self, x):        
        output= self.matcher(x)
        return output
