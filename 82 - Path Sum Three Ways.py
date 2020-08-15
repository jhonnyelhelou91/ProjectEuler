f = open('p082_matrix.txt', 'r')

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
cost = [0] * n

for i in range(0, n):
    cost[i] = matrix[i][n - 1]

for i in range(n - 2, -1, -1):
    cost[0] += matrix[0][i]
    for j in range(1, n):
        cost[j] = min([
            cost[j - 1] + matrix[j][i], cost[j] + matrix[j][i]
        ])
    for j in range(n - 2, -1, -1):
        cost[j] = min([
            cost[j], cost[j + 1] + matrix[j][i]
        ])

print(min(cost))
