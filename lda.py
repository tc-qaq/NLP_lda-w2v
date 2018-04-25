from gensim import corpora,models,matutils
from gensim.models.ldamulticore import LdaMulticore
from docutils.parsers.rst.directives import encoding
from gensim.models.ldamodel import LdaModel

count = 0;
fr = open("weibo_fenci_result.txt",'r',encoding="utf-8");
fo = open("weibo_vec_lda.txt",'w',encoding="utf-8");
id_list   = [];
data_list = [];

for line in fr.readlines():
    term = line.strip().split("\t")
    if( len(term) ==2 ):
        count += 1;
        id_list.append(term[0]);
        word = term[1].strip().split();
        data_list.append(word);

dic = corpora.Dictionary(data_list);               #construc dictionary
corpus = [dic.doc2bow(text) for text in data_list];#for each word sparse vec
tfidf = models.TfidfModel(corpus);                 #statistic ftidf

corpus_tfidf = tfidf[corpus];                      #get each text tfidf->sparse matrix

#500 can't generate a model so again 200;
#the max num of this is 300;
topic_nums = [10, 50, 80,100,150];
corpus_ldas = [];
for t_num in topic_nums:
    lda = LdaModel(corpus_tfidf,id2word = dic, num_topics = t_num); #generate LDA
    lda.save('weibo_lda'+str(t_num)+'.model');
    corpus_ldas.append(lda[corpus_tfidf]);

print("LDA has done!!!")

for corpus_lda in corpus_ldas:
    num = 0;
    for doc in corpus_lda:
        wstr = "";
        for i in range(len(doc)):
            item  = doc[i];
            wstr += str(item[0]) + ","+str(item[1])[0:7]+"/";
        fo.write(id_list[num]+"\t"+wstr[0:-1]+"\n");
        num += 1;
fr.close();
fo.close();
print("end"); 

