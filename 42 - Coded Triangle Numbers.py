# n2 + n - 2x = 0 => n = -1 + sqrt(1 + 8x) / 4
def isTriangular(x):
    return (-1 + (8 * x + 1) ** 0.5) % 4 == 0


def isWordTriangle(word):
    # trim quotes from start
    if (word[0] == '"'):
        word = word[1:]
    # trim quotes from finish
    if (word[-1] == '"'):
        word = word[:-1]
    word = word.lower()
    num = 0
    for c in word:
        num += 1 + ord(c) - ord('a')
    return isTriangular(num)


file1 = open('p042_words.txt', 'r')
words = file1.read().split(',')
file1.close()

count = 0
for word in words:
    if isWordTriangle(word):
        count += 1

print(count)
