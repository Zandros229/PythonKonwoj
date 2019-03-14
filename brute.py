import itertools


def perm(number_of_points):
    perm_tabel = [None] * (number_of_points + 1)
    for i in range(number_of_points):
        perm_tabel[i] = i;
    perm_tabel[number_of_points] = 0
    tab = []
    for permutatation in itertools.permutations(perm_tabel):
        if (permutatation.index(0) == 0) and (permutatation.index(0, 1) == number_of_points):
            tab.append(permutatation)
    return tab;


def brute_road(matrix, perm_tab):
    road_tab = []
    for index in range(len(perm_tabel)):
        road = 0
        for j in range(len(perm_tabel[index]) - 1):
            road += matrix[perm_tabel[index][j]][perm_tabel[index][j + 1]]
        road_tab.append(road)
        road_tab.sort()
    return road_tab


perm_tabel = perm(4)
print(perm_tabel)
