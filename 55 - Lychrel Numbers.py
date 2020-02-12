def isPalindrome(n):
    string = str(n)
    for i in range(0, len(string)):
        if string[i] != string[- 1 - i]:
            return False
    return True
def isLychrelNumber(n, iterations = 50):
    if iterations == 0:
        return True
    string = str(n)
    reverse = string[::-1]
    rev = int(reverse)

    if isPalindrome(n + rev):
        return False
    else:
        return isLychrelNumber(n + rev, iterations - 1)

n = 10000
result = 0
for i in range(1, n):
    if (isLychrelNumber(i)):
        result += 1

print (result)