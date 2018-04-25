#encoding= utf-8
import csv
import codecs
from idlelib.ReplaceDialog import replace
from idlelib.IOBinding import encoding
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.cluster import KMeans

fr = open('weibo_fenci_result.txt','r',encoding='utf-8');
id_list   = [];
data_list = [];
for line in fr.readlines():
    term = line.strip().split("\t");  
    if len(term) == 2 and term[1] !=" ":
        id_list.append(term[0]);
        data_list.append(term[1]);
hv = HashingVectorizer(n_features = 10000,non_negative=True);
post_tfidf = hv.fit_transform(data_list);
print ('Size of fea_train:' + repr(post_tfidf.shape));   
print (post_tfidf.nnz);
print ("tfidf has done!!!")

id = id_list;
tfidf_vec = post_tfidf;
kmean = KMeans(n_clusters = 300);
kmean.fit(tfidf_vec);
pred = kmean.predict(tfidf_vec);
print(pred);
fo = open("cluster.txt","a+",encoding="utf-8");
count = 0;
for i in range(len(pred)):
    count +=1;
    fo.write(id[i]+"\t"+str(pred[i])+"\n");
fo.close();

print(count);
print("kmeans cluster has done!!!")

