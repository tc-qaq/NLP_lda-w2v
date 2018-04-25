from _codecs import encode

fo1 = open("allstation_w2v2D.txt",'r',encoding='utf-8');
fo2 = open("allstation_w2v_label.txt",'r',encoding="utf-8");
fo3 = open('allstation_w2v2D_sampling_2.txt','r',encoding='utf-8');
fw = open("allstation_w2v_label_sampling_2.txt",'w',encoding="utf-8");

coord_2D = [];
label_2D = [];
samples = [];

for line in fo2.readlines():
    label_2D.append(line);
index=0;
for line in fo1.readlines():
    if(index > 0):
        term = line.strip().split(' ');
        coord_2D.append((term[0],term[1]));
    index +=1;
index=0;
for line in fo3.readlines():
    if(index > 0):
        term = line.strip().split(' ');
        samples.append((term[0],term[1]));
    index +=1;
labels = [];
index = 0;
for item1 in coord_2D:
    for item2 in samples:
        if(item1[0] == item2[0] and item1[1] == item2[1]):
            labels.append(label_2D[index]);
            fw.write(label_2D[index]);
    index +=1;
fw.close();
print(len(labels));