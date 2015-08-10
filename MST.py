from sys import argv
import re
import sys
import math

# Rounds number to the nearest integer
def nearest_int(num):
    if (num > 0):
        return int(num + .5)
    else:
        return int(num - .5)

# Calculates distance between city 1 and city 2
def calculate_distance(c1, c2):
    return nearest_int(math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2))

# Finds shortest tour using a greedy algorithm
def greedy_tsp(cities):

    total_distance = 0

    tour = list()
   
    keyy = {}
    parent = {}
    for k in cities:
        u = k
        break
    for v in cities:
        keyy[v] = calculate_distance(cities[u], cities[v])
        parent[v] = u
   
    for i in range(0, len(cities) - 1):
        minimum = sys.maxint
        vertex = None
        for v in cities:
            if keyy[v] > 0 and keyy[v] < minimum:
                minimum = keyy[v]
                vertex = v
        
        total_distance += minimum
        keyy[vertex] = 0
        temp = []
        temp.append(vertex)
        temp.append(parent[vertex])
        tour.append(temp)
        for v in cities:
            w = calculate_distance(cities[v], cities[vertex])
            if keyy[v] > w and w != 0:
                keyy[v] = w
                parent[v] = vertex
    
    return total_distance, tour

array_w_identifier=[]
array_wo_identifier=[]
fileName = 'tsp_example_1.txt' #change this before submit
if len(sys.argv) > 5:
    script, fileName = sys.argv[1]

outFile = fileName + '.result'
maps = {}
try:
    with open(fileName) as f:
        for line in f:
            for s in line.split(): 
                if s.isdigit():
                    array_w_identifier.append(int(s)) 
            maps[array_w_identifier[0]] = array_w_identifier[1:]
            del array_w_identifier[:]
            array_w_identifier[:] = []
except IOError as e:
    print 'Error in opening file '+ fileName
    sys.exit(-1)

#f2 = open(outFile,'w')

#print array_w_identifier
d, tour = greedy_tsp(maps)
print d
print tour
#print len(tour)==len(set(tour)) #just to check if we visited any city twice
print len(tour)
#f2.close()
