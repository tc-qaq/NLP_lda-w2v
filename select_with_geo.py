#encoding= utf-8
import jieba.analyse
import csv
import codecs
from idlelib.ReplaceDialog import replace
from idlelib.IOBinding import encoding
from sklearn.feature_extraction.text import HashingVectorizer

fr = open('weibo_status_hangzhou.csv','r',encoding='utf-8');
fo = open('weibo_status_hangzhou_wg.csv','a',encoding='utf-8',newline ='');
fo_writer = csv.writer(fo,delimiter = ",");

id_list_geo = [];
read = csv.reader(fr);
for str_l in read:
    if(len(str_l)>5 and ('_' in str_l[5]) and str_l[2] != "" and str_l[2] != ".." and str_l[2] != "..." and str_l[2] != "...." and str_l[2] != "分享图片"):
        id_list_geo.append(str_l[1]);
        fo_writer.writerow([str_l[0],str_l[1],str_l[2],str_l[3],str_l[4],str_l[5]]);
fr.close();
fo.close();
print(str(len(id_list_geo)) +"  geo discrimpt has done!!!");

