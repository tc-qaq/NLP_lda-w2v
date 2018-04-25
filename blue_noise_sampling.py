#encoding= utf-8
import random
import math
import pygame # draw point

import numpy as np  
from scipy import stats  
import copy


station_data = [];
samples = [];
active_list = [];
output_data =[];

def readData():
    fo1 = open("allstation_w2v2D.txt",'r',encoding="utf-8");    
    index = 0;
    for line in fo1.readlines():
        term = line.strip().split(' ');
        if (index > 0):
            station_data.append([float(term[0]),float(term[1])]);
        index +=1;
    v1 = [x[0] for x in station_data];v2 = [x[1] for x in station_data]; 
    max1 = max(v1);min1 = min(v1);max2 = max(v2);min2 = min(v2);
    nor1 = max1 - min1;nor2 = max2 - min2;
    index = 0;
    for item in station_data:
        x = station_data[index][0];
        y = station_data[index][1];
        station_data[index].append((x-min1)/nor1);
        station_data[index].append((y-min2)/nor2);
        station_data[index].append(0);
        index +=1;

def distance(p1, p2):
    p_diff = (p2[0] - p1[0], p2[1] - p1[1]);
    return math.sqrt(math.pow(p_diff[0], 2) + math.pow(p_diff[1], 2));
    
def is_in_circle(p):
    #d = distance(p, (0, 0));
    if(p[0]<1 and p[0]> 0 and p[1]< 1 and p[1]>0):
        return True;
    else:
        return False;

def generate_random_point(o, r,dataset):
    # Generate random point form dataset
    i = int(random.random()*len(dataset));
    ix = dataset[i][2];
    iy = dataset[i][3];
        
    return (ix, iy);

def generate_points(kde_function,dataset,radius):
    del samples[:];
#     for i in range(0,4500):
#         samples.append([dataset[i][2],dataset[i][3]]);
    len_s = len(dataset);
    # Choose a point randomly in the domain.
    initial_point = (0, 0);
    
    i  = int(random.random()*len_s);
    ix = dataset[i][2];
    iy = dataset[i][3];   
    initial_point = (ix, iy);
    samples.append(initial_point);
    dataset.pop(i);
    active_list.append(initial_point);
        
    while len(active_list) > 0:
        # Choose a random point from the active list.
        p_index = random.randint(0, len(active_list) - 1);
        random_p = active_list[p_index];
        
        found = False;        
        # Generate up to k points chosen uniformly at random from dataset
        k = 30
        for it in range(k):
            minimum_dist = float(kde_function(np.array(random_p))) * radius;
            pn = generate_random_point(random_p, minimum_dist,dataset);            
            fits = True;
            # TODO: Optimize.  Maintain a grid of existing samples, and only check viable nearest neighbors.
            for point in samples:
                if distance(point, pn) < minimum_dist:
                    fits = False;
                    break                    
            if fits:
                samples.append(pn);
                active_list.append(pn);
                index = 0;
                while (index < len(dataset)):
                    ix = dataset[index][2];
                    iy = dataset[index][3];
                    if(distance(pn, (ix,iy))< minimum_dist):
                       del(dataset[index]);
                    index+=1;
                found = True;
                print(str(len(samples)) + " :" + str(len(dataset)) + "-" + str(minimum_dist));
                break
        
        if not found:
            active_list.remove(random_p);
            if(len(samples)>6000):
                print(len(active_list));
    # Print the samples in a form that can be copy-pasted into other code.
    print("There are %d samples:" % len(samples))
    for point in samples:
        print("\t{\t%08f,\t%08f\t}," % (point[0], point[1]))

def labelData():
    index = 0;
    for item1 in station_data:
        for item2 in samples:
            if(item1[2] == item2[0] and item1[3] == item2[1]):
                station_data[index][4] = 1;
        index +=1;

def generate_data():
    fo  = open("allstation_w2v_name.txt",'r',encoding="utf-8");
    fw1 = open("allstation_w2v2D_sampling_2.txt",'w',encoding="utf-8");
    fw2 = open("allstation_w2v_name_sampling_2.txt",'w',encoding="utf-8");
    index = 0;
    for line in fo.readlines():
        station_data[index].append(line);
        index +=1;
    for item in station_data:
        if(item[4] == 1):
            output_data.append(item);
    fw1.write(str(len(output_data)) + " 2\n")
    for item in output_data:
        fw1.write(str(item[0])+ " "+str(item[1])+"\n");
        fw2.write(item[5]);
    fw1.close();
    fw2.close();

readData();

data1 = [];
for item in station_data:
    data1.append([item[0],item[1]]);
data1 = np.array(data1);
values = data1.T;  
kde = stats.gaussian_kde(values)    

print(float(kde(np.array([0,0]))));
#density = kde(values);

#min_dist = float(0.01);
gene_data = copy.deepcopy(station_data);
generate_points(kde,gene_data,150);

labelData();
generate_data();

print("end!");

# display
pygame.init();
screen = pygame.display.set_mode((500, 500));
clock = pygame.time.Clock();
while True:
    break_loop = False;
    clock.tick(60);    
    screen.fill((0,0,0));
    pygame.draw.circle(screen, (50, 50, 200), (250, 250), 250, 1);    
    for point in samples:
        lx = 250 + int((point[0]-0.5) * 250);
        ly = 250 + int((point[1]-0.5) * 250);
        pygame.draw.circle(screen, (255,255,255), (lx, ly), 2);
            
    pygame.display.flip();
    if break_loop:
        break