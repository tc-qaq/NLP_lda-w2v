#encoding= utf-8
from gensim.models import  word2vec
import logging

#main program 
# 11-12 month
# 29335 word types | 163952 raw words
# min_count=2 18k, min_count=5 8871, min_count=10 4443

#3 years
# 134371 word types | 9992989 raw words
# min_count=20 53k, min_count = 50

w_size = 100;
w_fre = 50;

logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)  
sentences =word2vec.Text8Corpus("allStationSentence.txt",max_sentence_length=100)  # loading   
model =word2vec.Word2Vec(sentences, size=w_size,min_count=w_fre)  # train skip-gram model default window=5  
print (model);

fo1 = open("w2v/allstation_w2v100D"+str(w_fre)+".txt",'w',encoding="utf-8");
fo2 = open("w2v/allstation_w2v_name"+str(w_fre)+".txt",'w',encoding="utf-8");

name_list =[];
vec_list = [];
#fo1.write(str(len(model.wv.vocab))+" 200 \n");
for item in model.wv.vocab:
    name_list.append(item);
    vec_list.append(model.wv[item]);
    str_vec = "";
    for v in model.wv[item]:
        str_vec += str(v) + " ";
    fo1.write(str_vec+"\n");
    fo2.write(item+"\n")
fo1.close();
fo2.close();
print(len(name_list));
print("end!!!");

  