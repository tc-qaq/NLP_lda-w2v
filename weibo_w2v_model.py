#encoding= utf-8
import gensim,codecs
from gensim.models import  word2vec
import logging

model =word2vec.Word2Vec.load("weibo_w2v.model");
fo1 = open("weibo_w2v200D.txt",'w',encoding="utf-8");
fo2 = open("weibo_w2v_id.txt",'w',encoding="utf-8");
print (model);
id_list =[];
vec_list =[];
fo1.write("29691 200 \n")
for item in model.wv.vocab:
    id_list.append(item);
    vec_list.append(model.wv[item]);
    str_vec = "";
    for v in model.wv[item]:
        str_vec += str(v) + " ";
    fo1.write(str_vec+"\n");
    fo2.write(item+"\n")
fo1.close();
fo2.close();
print(len(id_list));
print("end!!!");