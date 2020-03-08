from itertools import permutations

def get_magic_sum(numbers):
    count = len(numbers)
    half_count = int(count / 2)
    return (sum(numbers[half_count:count]) + 2 * sum(numbers[0:half_count])) / n

def convert_to_num(a, b, c, d, e, f, g, h, i, j):
    big_num = {a:0, d:1, f:2, h:3, j:4}
    break_num = big_num[min(big_num.keys())]
    nums = [(a,b,c), (d,c,e), (f,e,g), (h,g,i), (j,i,b)]
    nums = nums[break_num:]+nums[:break_num]
    string = ''
    for num_tup in nums:
        for num in num_tup:
            string += str(num)
    
    return string

n = 5
numbers = range(1, 2 * n + 1)
magic_sum = get_magic_sum(numbers)
result = 0

for a in numbers:
    b_numbers = [number for number in numbers if number != a]
    for b in b_numbers:
        c_numbers = [number for number in b_numbers if number != b]
        for c in c_numbers:
            #check first set
            if a + b + c == magic_sum:
                d_numbers = [number for number in c_numbers if number != c]
                for d in d_numbers:
                    e_numbers = [number for number in d_numbers if number != d]
                    for e in e_numbers:
                        #check second set
                        if c + d + e == magic_sum:
                            f_numbers = [number for number in e_numbers if number != e]
                            for f in f_numbers:
                                g_numbers = [number for number in f_numbers if number != f]
                                for g in g_numbers:
                                    #check third set
                                    if e + f + g == magic_sum:
                                        h_numbers = [number for number in g_numbers if number != g]
                                        for h in h_numbers:
                                            i_numbers = [number for number in h_numbers if number != h]
                                            for i in i_numbers:
                                                #check fourth set
                                                if g + h + i == magic_sum:
                                                    j_numbers = [number for number in i_numbers if number != i]
                                                    for j in j_numbers:
                                                        #check fifth set
                                                        if b + i + j == magic_sum:
                                                            valid_number = int(convert_to_num(a, b, c, d, e, f, g, h, i, j))
                                                            if result < valid_number:
                                                                result = valid_number

print (result)