import random

width = 10
matrix = [[random.randint(-100, 100) for _ in range(10)] for _ in range(10)]
matrix_1 = [[random.randint(-100, 100) for _ in range(10)] for _ in range(10)]
matrix_2 = []

def pl(m):
    for i in m:
        print(i)

for i in range(len(matrix)):
    matrix_2.append([])
    for j in range(len(matrix[i])):
        matrix_2[i].append([])
        matrix_2[i][j] = matrix[i][j] + matrix_1[i][j]
        
pl(matrix)
print("Matrix")
pl(matrix_1)
print("Matrix sum")
pl(matrix_2)