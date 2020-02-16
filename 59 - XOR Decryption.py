import string, itertools


def xorEncryption(c, key):
    result = c ^ key
    char = chr(result)
    if char in alpha_low or char in alpha_up or char in others:
        return True
    return False


def isValidKey(cipher, key):
    length = len(key)
    text = 0
    for i in range(0, len(cipher)):
        k = key[i % length]
        k_ord = ord(k)
        if not xorEncryption(cipher[i], k_ord):
            return 0
        else:
            text += cipher[i] ^ k_ord
    return text

def decrypt(cipher, n):
    keys = [''.join(x) for x in map(list, itertools.permutations(alpha_low, n))]

    for key in keys:
        decrypted = isValidKey(cipher, key)
        if decrypted != 0:
            return decrypted
    return ''

f = open('p059_cipher.txt', 'r')

cipher = [int(x) for x in f.read().strip().split(',')]
alpha_low = string.ascii_lowercase
alpha_up = string.ascii_uppercase
others = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '|', '%', '`',
          ' ', ';', ':', ',', '.', '?', "'", '\"', '-', '&', '(', ')', '{', '}', '[', ']']
n = 3
result = decrypt(cipher, n)

#129448
print('result:', result)