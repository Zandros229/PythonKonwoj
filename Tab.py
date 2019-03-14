import math
import random


def random_points(number_of_Points):
    tab = [[None] * 3] * number_of_Points
    for index in range(number_of_Points):
        tab[index] = [index, math.trunc(random.uniform(1, 100)), math.trunc(random.uniform(1, 100))]
    return tab


def distance_points(a, b):
    return math.sqrt((a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)


def distance_list(a, b, size):
    tab=[None]*size
    for index in range(size):
        tab[index] = distance_points(a, b[index])
    return tab


def distance_matrix(tab, number_of_Points):
    matrix = [[None] * number_of_Points] * number_of_Points
    for index in range(number_of_Points):
        matrix[index] = distance_list(tab[index], tab, number_of_Points)
    return matrix


tab = random_points(4)
print(tab)
print(distance_points(tab[0], tab[1]))
matrix = distance_matrix(tab, 4)
print(matrix)
