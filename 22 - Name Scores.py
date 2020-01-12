def nameScore(name, index):
    score = 0
    for c in name:
        score += 1 + ord(c) - ord('A')
    return score * index

file1 = open('p022_names.txt', 'r')
result = 0
index = 0

names = file1.read().split(',')
file1.close()
names.sort()

for name in names:
    #trim quotes from start
    if (name[0] == '"'):
        name = name[1:]
    #trim quotes from finish
    if (name[-1] == '"'):
        name = name[:-1]
    index = index + 1
    result += nameScore(name, index)

print (result)