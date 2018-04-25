#encoding= utf-8
import jieba.analyse
import csv
import codecs
from idlelib.ReplaceDialog import replace
from idlelib.IOBinding import encoding
from sklearn.feature_extraction.text import HashingVectorizer

f1 = open('weibo_fenci_result.txt','a',encoding='utf-8');
i  = 1;

stopwords = codecs.open('stopwords.txt','r',encoding='utf8').readlines()
stopwords = [ w.strip() for w in stopwords ]

with open('weibo_status_hangzhou.csv','r',encoding="utf-8",newline='') as csvfile:
    read = csv.reader(csvfile)
    for str in read:
        if(len(str) >2 and str[2] != "" and str[2] != ".." and str[2] != "..." and str[2] != "...."):
            key_list = jieba.analyse.extract_tags(str[2],30);
            if(len(key_list) > 0):
                ustr = str[1]+"\t"
                for i in key_list:
                    if (i not in stopwords):
                        ustr += i + " ";
                f1.write(ustr+"\n");
f1.close();
print("weibo_feici_key_word has done!!!");





