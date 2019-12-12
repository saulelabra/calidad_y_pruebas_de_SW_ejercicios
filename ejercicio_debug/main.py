import sys

#def union2D(list, ref):
    

f = open("points.txt", "r")
points = []

for line in f:
    ind_point = line.split()
    ind_point[0] = int(ind_point[0])
    ind_point[1] = int(ind_point[1])
    points.append(ind_point)

print(points)