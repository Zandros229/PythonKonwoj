import copy
import itertools
import math
import random
import heapq
import numpy
import brute
import dfs


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
    print(matrix)
    for index in range(number_of_points):
        matrix[index] = distance_list(tab[index], tab, number_of_points)
    return matrix


def nearest(matrix, number_of_points):
    used = [None] * (number_of_points + 1)
    tab = copy.deepcopy(matrix)
    used[0] = 0
    road = 0
    j = 1
    helper = False
    index = 0
    helper2 = False
    for i in range(number_of_points):
        tab[index].sort()
    while not helper:
        helper2 = False
        i = 1
        while not helper2:
            value = tab[index][i]
            temp = (matrix[index] == value)
            point = list(temp).index(True)
            if point not in used:
                used[j] = point
                road += value
                helper2 = True
                j += 1
                index = point
            else:
                i += 1
        if used[number_of_points - 1] is not None:
            helper = True
            road += matrix[used[number_of_points - 1]][0]
            used[number_of_points] = 0
    return road


tab = random_points(4)
print(tab)
# NN
matrix = distance_matrix(tab, 4)
near = nearest(matrix, 4)
print(matrix)
print(nearest(matrix, 4))
# Brute Force

perm_tabel = brute.perm(4)
road = brute.brute_road(matrix, perm_tabel)
print(perm_tabel)
print(brute.brute_road(matrix, perm_tabel))


#DFS
distance=dfs.road_dfs(4)
print(dfs.road_dfs(4))
distance=dfs.dfs_distance(matrix,distance)
print(distance)

