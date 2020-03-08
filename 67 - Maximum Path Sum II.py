f = open('p067_triangle.txt', 'r')

lines = f.readlines()
triangle = [x.strip().split(' ') for x in lines]
for i in range(0, len(triangle)):
    for j in range(0, len(triangle[i])):
        triangle[i][j] = int(triangle[i][j])

for x in range(len(triangle) - 2, -1, -1):
    for y in range(0, x + 1):
        if (triangle[x + 1][y] > triangle[x + 1][y + 1]):
            triangle[x][y] += triangle[x + 1][y]
        else:
            triangle[x][y] += triangle[x + 1][y + 1]

print (triangle[0][0])