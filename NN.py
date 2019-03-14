import copy


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
