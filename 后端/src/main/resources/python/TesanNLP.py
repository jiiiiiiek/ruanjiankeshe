from put_into_application import get_batch
from put_into_application import make_mask
import torch
import pickle
from parameter import parse_args
from load_data import load_text
from torch.autograd import Variable


def TeNLP(text):
    net = torch.load('F:\\testweb\\demo\\src\\main\\resources\\python\\net_cn2.bin')
    text_len=len(text)
    zero = [0]
    zero_list = [zero]*text_len
    zero_tensor = torch.tensor(zero_list).float()
    args = parse_args()
    net.eval()
    text_data=load_text(text)
    g = open('F:\\testweb\\demo\\src\\main\\resources\\python\\w2v_cn.txt', 'rb')
    w2v_model=pickle.load(g)
    all_indices = torch.arange(text_len).long().split(args.batch_size)
    out_tensor=torch.empty(0)
    out_tensor=out_tensor.to('cuda:0')


    for batch_indices in all_indices:
        with torch.no_grad():
            batch_x = get_batch(text_data, w2v_model, batch_indices)
            # get_batch=text,m2v,1000+b_ind(text的第几维）
            batch_x = Variable(torch.from_numpy(batch_x).float()).cuda()
            batch_mask = make_mask(text_data, batch_indices, batch_x.shape[1])
            # make_mask=text,1000+b_ind,batch_x的第二维长度
            batch_mask = Variable(torch.from_numpy(batch_mask).float()).cuda()

            input = Variable(zero_tensor[batch_indices]).cuda()  # data_bow需要

            recon, loss, out = net(input, batch_x, batch_mask, compute_loss=True)  # 三位输出

            out = torch.nn.functional.softmax(out, dim=1)
            out_tensor = torch.cat((out_tensor,out),dim=0)

    return out_tensor


