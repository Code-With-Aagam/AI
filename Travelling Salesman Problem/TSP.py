import tsp
matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
r = range(len(matrix))
shortestpath = {(i,j):matrix[i][j] for i in r for j in r }
print(tsp.tsp(r,shortestpath))
