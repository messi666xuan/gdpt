import sys
import torch
import torchvision
print("torchvision version:",torchvision. __version__)
print("python版本:",sys.version)
print("torch version:",torch.__version__)
print("gpu可用:",torch.cuda.is_available())
print('CUDA version:',torch.version.cuda)
print("安装环境是按次服务，禁止进行修改或者删除操作，如果更换或者删除不属于售后范围")