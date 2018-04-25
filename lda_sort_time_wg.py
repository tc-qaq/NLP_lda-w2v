#coding:utf-8
import csv
import codecs
from idlelib.ReplaceDialog import replace
from idlelib.IOBinding import encoding
import datetime,time, operator

fr = open("weibo_vec_lda.txt",'r',encoding="utf-8");
fo = open("weibo_vec_lda_wg.txt",'w',encoding="utf-8");

weibo_data = [];
with open('weibo_status_hangzhou_wg.csv','r',encoding="utf-8",newline='') as csvfile:
    read = csv.reader(csvfile)
    for str in read:
        if(str[0] != "created_at"):            
            weibo_data.append({'created_at':str[0],'id':str[1],'text':str[2],'source':str[3],'user_id':str[4],'place_id':str[5]});

weibo_data.sort(key=lambda item: int(time.mktime(datetime.datetime.strptime(item['created_at'], '%Y-%m-%d %H:%M:%S+08').timetuple())));
print(weibo_data[0]);
print(weibo_data[len(weibo_data)-1]);
print("sort time has done!!!");

lda_data =[];
for line in fr.readlines():
    term = line.strip().split("\t");
    lda_data.append(term);

lda_wg_data =[];

for index in lda_data:
    for line in weibo_data:
        if(index[0] == line['id'] and len(index) == 2 and index[1] !=' 'and index[1] !='  '):
            fo.write(index[0]+"\t"+index[1]+"\n");
            break;
fo.close();
print("end!");


