from sklearn.manifold import TSNE

fo2 = open("allstation_w2v100D.txt",'r',encoding="utf-8");
fw = open("allstation_w2v2D_1.txt",'w',encoding="utf-8");
vec_list =[];
for line in fo2.readlines():
    term = line.strip().split(" ");
    arr = [];
    for num in term:
        arr.append(float(num));
    vec_list.append(arr);

tsne=TSNE(metric='cosine', method='barnes_hut', angle=0.2);#metric='cosine', method='barnes_hut', angle=0.2

data_tsne = tsne.fit_transform(vec_list)  
print(data_tsne);
fw.write(str(len(data_tsne))+" 2 \n");
for line in data_tsne:
    fw.write(str(line[0])+" "+str(line[1])+"\n");
print("end!")
fw.close();


