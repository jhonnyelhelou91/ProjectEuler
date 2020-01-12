counts = {
    0: 0,
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}
def letterCount(n):
    if (n > 10000):
        print ('above 1000 is not currently supported')
        return ''

    if (n >= 1000):
        digit = int(n % 1000)
        count = letterCount(int(n / 1000)) + ' thousand '
        if (digit > 0):
            count += ' and ' + letterCount(digit)
        return count 
    if (n >= 100):
        digit = int(n % 100)
        count = letterCount(int(n / 100)) + ' hundred '
        if (digit > 0):
             count += ' and ' + letterCount(digit)
        return count
    if (n in counts):
        return counts[n]
    if (n < 100):
        digit = n % 10
        return letterCount(n - digit) + ' ' + letterCount(digit)

n = 1001
count = 0
for x in range(1, n):
   count += len(letterCount(x).replace(' ', ''))

print(count)