import torch

a = torch.rand(2,3)
print(a)

b = torch.randn(2, 3)
print(b)

c = torch.normal(0, 1, (2, 3))
print(c)

d = torch.Tensor(2,2).uniform_(-5, 5)
print(d)

