import math
import random


def random_points(number_of_Points):
    tab = [[None] * 3] * number_of_Points
    for index in range(number_of_Points):
        tab[index] = [index, math.trunc(random.uniform(1, 100)), math.trunc(random.uniform(1, 100))]
    return tab


tab = random_points(4)
print(tab)
