import torch.nn
import torch.nn.functional as F
import torch.optim as optim

class Match_encoder(torch.nn.Module):
    def __init__(self):
        super(Match_encoder,self).__init__()
        input_dim=1000
        Hidden_dim=500
        output_dim=3
        self.matcher=torch.nn.Sequential(
            torch.nn.Linear(input_dim,Hidden_dim),
            torch.nn.Linear(Hidden_dim,2*Hidden_dim),
            torch.nn.ReLU(),
            torch.nn.Linear(2*Hidden_dim,Hidden_dim),
            torch.nn.Linear(Hidden_dim,output_dim),
            torch.nn.Softmax(dim=2))
    
    def forward(self, x):        
        out= self.matcher(x)
        return out
