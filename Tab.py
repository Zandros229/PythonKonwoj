import math
import random


def random_points(number_of_Points):
    tab = [[None] * 3] * number_of_Points
    for index in range(number_of_Points):
        tab[index] = [index, math.trunc(random.uniform(1, 100)), math.trunc(random.uniform(1, 100))]
    return tab
def distance_in_cart(tab, number_of_Points):
    matrix=[[None] * number_of_Points] * number_of_Points
    for index_in_row in range(number_of_Points):
        for index_in_column in range(number_of_Points):
            matrix[index_in_row][index_in_column]=math.sqrt((tab[index_in_row][1]-tab[index_in_column][1])**2+(tab[index_in_row][2]-tab[index_in_column][2])**2)
    return matrix


tab = random_points(4)
print(tab)
matrix=distance_in_cart(tab,4)
print(matrix)

