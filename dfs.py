

def road_dfs(number_of_points):
    tabel = [None] * (number_of_points)
    for i in range(number_of_points):
        tabel[i] = i
    used=[]
    road=[]
    i=1
    used.append(0)
    while len(used)<number_of_points:
        if tabel[i] not in used:
            road.append(tabel[i])
            used.append(tabel[i])
            i=1
        elif i<number_of_points-1:
            i+=1
    used.append(0)
    return used

def dfs_distance(matrix, road):
    distance=0
    for j in range(len(road) - 1):
        distance += matrix[road[j]][road[j + 1]]
    return distance
