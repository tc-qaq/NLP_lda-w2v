#coding:utf-8
import csv
import codecs
from idlelib.ReplaceDialog import replace
from idlelib.IOBinding import encoding

fr = open("weibo_vec_lda_wg.txt",'r',encoding="utf-8");
fo = open("weibo_w2v.txt",'w',encoding="utf-8");

lda_data =[];
for line in fr.readlines():
    term = line.strip().split("\t");
    lda_data.append(term);
weibo_w2v = [];
for i in range(81):
    sentence ="";
    for line in lda_data:
        if(len(line) == 2):
            term = line[1].strip().split("/");
            for t_str in term:
                temp = int(t_str[:t_str.find(',')]);
                if(i == temp):
                    sentence += ''.join(line[0]+' ');
    weibo_w2v.append(sentence);
print("sentence generation has done!!!")

for index in weibo_w2v:
    fo.write(index +"\n");

fo.close();
print("end!");
