#encoding= utf-8
from gensim.models import  word2vec
import logging

#main program 
logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)  
sentences =word2vec.Text8Corpus(u"stationSentence.txt")  # loading   
model =word2vec.Word2Vec(sentences, size=200)  # train skip-gram model default window=5  
print (model);

fo1 = open("station_w2v200D.txt",'w',encoding="utf-8");
fo2 = open("station_w2v_name.txt",'w',encoding="utf-8");

name_list =[];
vec_list = [];
fo1.write("447 200 \n")
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


# 计算两个词的相似度/相关程度  
#try:  
#    y1 = model.similarity(u"赵敏", u"周芷若")  
#except KeyError:  
#    y1 = 0  
#print (u"【赵敏】和【周芷若】的相似度为：", y1)  
#print("-----\n")  
#  
# 计算某个词的相关词列表  
#y2 = model.most_similar(u"赵敏", topn=20)  # 20个最相关的  
#print (u"和【赵敏】最相关的词有：\n")  
#for item in y2:  
#    print (item[0], item[1])  
#print("-----\n")  


   
# 保存模型，以便重用  
#model.save(u"书评.model")
#model.wv.save_word2vec_format(u"书评.vector", binary=False)
  