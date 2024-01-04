# -*- coding: utf-8 -*-

from TesanNLP import TeNLP

#text=sys.argv[1]
f=open("F:\\testweb\\demo\\src\\main\\resources\\python\\Content.txt",'r',encoding='utf-8')
text=[]
text.append(f.readline())
f.close()
out=TeNLP(text)
f=open("F:\\testweb\\demo\\src\\main\\resources\\python\\motion.txt",'w')
data=out.tolist()[0]
for i in range(6):
    f.write(str(data[i])+"\n")
f.close()