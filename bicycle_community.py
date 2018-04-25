from _codecs import encode
import numpy
import argparse
import matplotlib.pyplot as plt
fo1 = open("All_data_community.csv",'r',encoding="utf-8");
fo2 = open("allstation_w2v_name_sampling_2.txt",'r',encoding="utf-8");
fw = open("allstation_w2v_label_sampling_2.txt",'w',encoding="utf-8");

dict_stations = {};
index = 0;
for line in fo1.readlines():
    term = line.strip().split(",");    
    index += 1;
    if (index > 1 ):
        dict_stations[term[1]] = term[2];
label_list =[];
for line in fo2.readlines():
    term = line.strip().split("-");
    if(dict_stations[term[0]] == dict_stations[term[1]]):
        label = dict_stations[term[0]];
    else:
        label = "-1";
    label_list.append(label);
    fw.write(label + "\n");
print("end!");


l1 = label_list;
l2 = [];
[l2.append(i) for i in l1 if not i in l2] 
print(len(l2));
print(l2);
