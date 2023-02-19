#!/usr/bin/python3

import sys
import gzip
import pickle

if(len(sys.argv) < 3):
    print("./Snap2MetisPy3.py input-file output-file [current version works only on unweighted graph.]")
    sys.exit(0)

if sys.argv[1][-2:] == "gz":
    in_file = gzip.open(sys.argv[1], "rt")
else:
    in_file = open(sys.argv[1], "rt")

out_file = open(sys.argv[2], "w")

directed = False 
dic = {}
id_map = {} 
node_num = 4039
edge_num = 88234

for line in in_file:
    if("#" in line):
        if("Nodes" in line):
            str_split = line.strip().split()
            node_num = int(str_split[2])
            edge_num = int(str_split[4])
            print(node_num, edge_num)
        continue
    str_split = [int(ele) for ele in line.strip().split()]
    if(str_split[0] == str_split[1]):
        continue
    if(str_split[0] in dic):
        dic[str_split[0]].append(str_split[1])
    else:
        dic[str_split[0]] = []
        dic[str_split[0]].append(str_split[1])
    if(directed == False):
        if(str_split[1] in dic):
            dic[str_split[1]].append(str_split[0])
        else:
            dic[str_split[1]] = []
            dic[str_split[1]].append(str_split[0])

count = 1 
key_set = [ele for ele in dic]
for ele in key_set:
    id_map[ele] = count
    count += 1

print("Finish reading graph...")
print(node_num, count-1)

edge_count = 0
for key in key_set:
    tmp_set = set(dic[key])
    for ele in tmp_set:
        edge_count += 1
edge_num = edge_count//2

print(str(count-1) + " " + str(edge_num), file=out_file)
print(max(ele for ele in dic))

truth_edge = 0
for key in key_set:
    out_line = ""
    tmp_set = set(dic[key])
    truth_edge += len(tmp_set)
    for ele in tmp_set:
        out_line += str(id_map[ele]) + " "
    out_file.write(out_line.strip() + "\n")

if(edge_count != 2*edge_num):
    print("Wrong edge num: " + str(edge_num) + " vs. " + str(edge_count) + " (count)")
print("Output metis file contains edges: " + str(truth_edge/2))
out_file.close()
in_file.close()
objFile = open("map.obj", "wb")
pickle.dump(id_map, objFile)
objFile.close()
