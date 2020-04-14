import torch.nn
import torch.nn.functional as F
import torch.optim as optim

class Preprocessor(torch.nn.Module):
    def __init__(self):
        super(Preprocessor,self).__init__()
        input_dim=503
        output_dim=500
        self.preprocess=torch.nn.Sequential(
            torch.nn.Linear(input_dim,output_dim))
            
    
    def forward(self, x):        
        out= self.preprocess(x)
        return out