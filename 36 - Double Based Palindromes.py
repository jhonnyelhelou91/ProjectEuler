def isPalindrome(n):
    count = len(n)
    for i in range(0, count):
        if (n[i] != n [count - i - 1]):
            return False
    return True

def isDoubleBasedPalindrome(n):
    if (isPalindrome(str(n))):
        return isPalindrome(bin(x)[2:])
    return False

n = 1000000
result = 0

for x in range(1, n):
    if (isDoubleBasedPalindrome(x)):
        result += x

print (result)