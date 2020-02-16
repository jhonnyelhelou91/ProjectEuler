def permutationKey(n):
    string = str(n)
    key = ''
    for digit in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        key += digit + ':' + str(string.count(digit)) + ' '
    return key.strip()

n = 5
cubes = {}
x = 2
while True:
    cube = x ** 3
    key = permutationKey(cube)
    if key not in cubes:
        cubes[key] = set([cube])
    else:
        cubes[key].add(cube)
        if len(cubes[key]) == n:
            print (sorted(cubes[key])[0])
            break
    x += 1