import jieba
import codecs
from idlelib.ReplaceDialog import replace
from idlelib.IOBinding import encoding
#中文编码问题，就是都用同一种编码就好了，如下都用encodeing='utf-8'实现中文的读写
f1 = open('fenci.txt','r+',encoding="utf-8");
f2 = open('fenci_result.txt','a',encoding='utf-8');
lines = f1.readlines();
for line in lines:
    line.replace('\t', '').replace('\n', '').replace(' ','');
    seg_list = jieba.cut(line, cut_all=False);
    str_out = " ".join(seg_list)  
    #print(str_out); 
    
    f2.write(str_out);
f1.close();
f2.close();