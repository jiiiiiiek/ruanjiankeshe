import torch
import numpy as np
from parameter import parse_args
import torch.optim as optim
import pickle
import torch.nn as nn
from torch.autograd import Variable

args = parse_args()
args.in_dim=100
args.h_dim=200

g = open('F:\\testweb\\demo\\src\\main\\resources\\python\\w2v_cn.txt', 'rb')
w2v_model=pickle.load(g)

# load data for NTM
zero = [0] * 3320
zero_list=[zero]
zero_tensor = torch.tensor(zero_list).float()

# print('Data loaded')


def get_batch(text_data, w2v_model, indices):
    batch_size = len(indices) # 批次大小，即索引列表长度
    text_length = []
    for idx in indices:
        text_length.append(len(text_data[idx])) # 每条数据的长度
    batch_x = np.zeros((batch_size, max(text_length), args.in_dim), dtype=np.float32) # batch_x全零数组，，第一个参数为形状
    # 其形状为batch_size批次中的样本数 X max(text_length) 批次中文本的最大长度 X args.in_dim 词向量特征维度=300
    for i, idx in enumerate(indices, 0):
        for j, word in enumerate(text_data[idx], 0):
            if word in w2v_model:
                batch_x[i][j] = w2v_model[word]
            else:
                # handle unknown words here, for example, assign a zero vector
                batch_x[i][j] = np.zeros(args.in_dim)  # Replace this with your handling logic

    return batch_x # batch_x是一个npy数组


def make_mask(text_data, indices, sent_length):
    batch_size = len(indices)
    text_length = [len(text_data[idx]) for idx in indices]
    mask = np.full((batch_size, sent_length, 1), float('-inf'), dtype=np.float32)
    for i in range(batch_size):
        mask[i][0:text_length[i]] = 0.0
    return mask

# anger, disgust, fear, joy, sadness, surprise

# CN/ZH:
# 感动 ， 震惊 ， 搞笑 ， 难过 ， 新奇 ， 愤怒? ########
# touch,surprise,amusement,sadness,curiosity,anger
