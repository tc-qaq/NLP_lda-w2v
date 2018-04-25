#encoding= utf-8
import gensim,codecs
from gensim.models import  word2vec
import logging

#main program 
logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)  
sentences =word2vec.Text8Corpus(u"weibo_w2v.txt")  # loading   
model =word2vec.Word2Vec(sentences, size=200)  # train skip-gram model ��default window=5  
   
print (model);
#for item in model.wv.vocab:
#    print(item);

weibo_data = [];
fr = open("weibo_status_hangzhou_wg.csv",'r',encoding="utf-8");
for line in fr.readlines():
    term = line.strip().split(",");
    weibo_data.append(term);
weibo1 = [];
weibo2 = [];
for line in weibo_data:
    if(line[1] == '3614534168327991'):
        weibo1 = line;
    if(line[1] == '3555781717053113'):
        weibo2 = line;
# 计算两个词的相似度/相关程度  
try:  
    y1 = model.wv.similarity(u"3614534168327991", u"3555781717053113")  
except KeyError:  
    y1 = 0  
print(weibo1);
print(weibo2);
print (u"【3614534168327991】和【3555781717053113】的相似度为：", y1)  
print("-----\n")  
#  
# 计算某个词的相关词列表  
y2 = model.most_similar(u"3614534168327991", topn=20)  # 20个最相关的  
print (u"和【3614534168327991】最相关的词有：\n")  
for item in y2:  
    for line in weibo_data:
        if(item[0] == line[1]):
            print(line);
    print (item[0], item[1])  
print("-----\n")  
   
# 寻找对应关系  
#print (u"张无忌-张三丰，赵敏-")  
#y3 =model.most_similar([u'张无忌', u'张三丰'], [u'赵敏'], topn=3)  
#for item in y3:  
#    print (item[0], item[1])  
#print("----\n")  
   
# 寻找不合群的词  
#y4 =model.doesnt_match(u"张无忌 张三丰 赵敏 屠龙".split())  
#print (u"不合群的词：", y4)  
#print("-----\n")

# 保存模型，以便重用  
model.save(u"weibo_w2v.model")
model.wv.save_word2vec_format(u"weibo_w2v.vector", binary=False)
# 对应的加载方式  
# model_2 =word2vec.Word2Vec.load("weibo_w2v.model")  
