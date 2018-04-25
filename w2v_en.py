#encoding= utf-8
from gensim.models import  word2vec
import logging

#main program 
logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)  
sentences =word2vec.Text8Corpus(u"text8")  # loading   
model =word2vec.Word2Vec(sentences, size=200)  # train skip-gram model ��default window=5  
   
print (model);
# 计算两个词的相似度/相关程度  
try:  
    y1 = model.similarity(u"woman", u"man")  
except KeyError:  
    y1 = 0  
print (u"【woman】和【man】的相似度为：", y1)  
print("-----\n")  
#  
# 计算某个词的相关词列表  
y2 = model.most_similar(u"good", topn=20)  # 20个最相关的  
print (u"和【good】最相关的词有：\n")  
for item in y2:  
    print (item[0], item[1])  
print("-----\n")  
   
# 寻找对应关系  
print (u"boy-father，girl-")  
y3 =model.most_similar([u'boy', u'father'], [u'girl'], topn=3)  
for item in y3:  
    print (item[0], item[1])  
print("----\n")  
   
# 寻找不合群的词  
y4 =model.doesnt_match(u"breakfast cereal dinner lunch".split())  
print (u"不合群的词：", y4)  
print("-----\n")
   
# 保存模型，以便重用  
model.save(u"text8.model")
model.wv.save_word2vec_format(u"text8.vector", binary=False)
# 对应的加载方式  
# model_2 =word2vec.Word2Vec.load("text8.model")  
   
# 以一种c语言可以解析的形式存储词向量  
#model.save_word2vec_format(u"书评.model.bin", binary=True)  
# 对应的加载方式  
# model_3 =word2vec.Word2Vec.load_word2vec_format("text8.model.bin",binary=True)   