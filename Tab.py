import copy
import itertools
import math
import random
import heapq
import time

import numpy
import brute
import dfs
import NN


def random_points(number_of_Points):
    tab = [[None] * 3] * number_of_Points
    for index in range(number_of_Points):
        tab[index] = [index, random.uniform(1, 100), random.uniform(1, 100)]
    return tab


def distance_points(a, b):
    return math.sqrt((a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)


def distance_list(a, b, size):
    tab = [None] * size
    for index in range(size):
        tab[index] = distance_points(a, b[index])
    return tab


def distance_matrix(tab, number_of_points):
    # matrix = [[None] * number_of_points] * number_of_points
    matrix = numpy.zeros((number_of_points, number_of_points))
    for index in range(number_of_points):
        matrix[index] = distance_list(tab[index], tab, number_of_points)
    return matrix



# NN

nn_resoult=[]
tab=[]
matrix=[]
for j in range(4,11):
    tab.append(random_points(j))
i=0
for j in range(4,11):
     matrix.append(distance_matrix(tab[i], j))
     i+=1
i=0
for j in range(4,11):
    start=time.time_ns()
    near = NN.nearest(matrix[i], j)
    stop=time.time_ns()
    nn_resoult.append([j,near,(stop-start)])
    i+=1


print(nn_resoult)

# matrix = distance_matrix(tab, 4)
# near = NN.nearest(matrix, 4)
# print(matrix)
# print(NN.nearest(matrix, 4))
# Brute Force

# perm_tabel = brute.perm(4)
# road = brute.brute_road(matrix, perm_tabel)
# print(perm_tabel)
# print(brute.brute_road(matrix, perm_tabel))
#
# # DFS
# distance = dfs.road_dfs(4)
# print(dfs.road_dfs(4))
# distance = dfs.dfs_distance(matrix, distance)
# print(distance)
