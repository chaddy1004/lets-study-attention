import torch
from torch import nn
from torch.nn import Module, ModuleDict, ModuleList

d_model = 512
n_heads = 6
a = nn.TransformerEncoderLayer(d_model=d_model, nhead=n_heads)


class Attention(Module):
    def __init__(self, q, k, v):
        super().__init__()
        pass

    def forward(self):



class TransformerEncoderLayerScratch(Module):

