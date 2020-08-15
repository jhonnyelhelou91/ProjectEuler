f = open('p081_matrix.txt', 'r')

lines = f.readlines()

# matrix = [
#    [ 131, 673, 234, 103, 18 ],
#    [ 201, 96, 342, 965, 150 ],
#    [ 630, 803, 746, 422, 111 ],
#    [ 537, 699, 497, 121, 956 ],
#    [ 805, 732, 524, 37, 331 ],
# ]
matrix = [[int(num) for num in line.split(',')] for line in lines]
n = len(matrix)

for i in range(n - 2, -1, -1):
    matrix[n - 1][i] += matrix[n - 1][i + 1]
    matrix[i][n - 1] += matrix[i + 1][n - 1]

for i in range(n - 2, -1, -1):
    for j in range(n - 2, -1, -1):
        matrix[i][j] += min([
            matrix[i + 1][j], matrix[i][j + 1]
        ])

print(matrix[0][0])
