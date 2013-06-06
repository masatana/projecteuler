# -*- coding: utf-8 -*-

mat = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

for i in range(1, 21):
    mat.append([0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

new_dict = {}
for i in range(2, 22):
    for j in range(2, 22):
        print mat[i - 1][j] + mat[i][j - 1]
        mat[i][j] = mat[i - 1][j] + mat[i][j - 1]

for row in mat:
    print row
