result = 0
d1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
d3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
d4 = [0, 2, 4, 6]
#(d3 + d4 + d5) % 3 == 0
d5 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
d6 = [0, 5]
d7 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
d8 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
d9 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
d0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# d5d6d7 % 7 == 0
# d6d7d8 % 11 == 0
# d7d8d9 % 13 == 0
# d8d9d10 % 17 == 0

for _d1 in d1:
    for _d2 in d2:
        if _d1 != _d2:
            for _d3 in d3:
                if _d1 != _d3 and _d2 != _d3:
                    for _d4 in d4:
                        if _d1 != _d4 and _d2 != _d4 and _d3 != _d4:
                            for _d5 in d5:
                                if _d1 != _d5 and _d2 != _d5 and _d3 != _d5 and _d4 != _d5 and (_d3 + _d4 + _d5) % 3 == 0:
                                    for _d6 in d6:
                                        if _d1 != _d6 and _d2 != _d6 and _d3 != _d6 and _d4 != _d6 and _d5 != _d6:
                                            for _d7 in d7:
                                                if _d1 != _d7 and _d2 != _d7 and _d3 != _d7 and _d4 != _d7 and _d5 != _d7 and _d6 != _d7 and (_d5 * 100 + (_d6 * 10) + _d7) % 7 == 0:
                                                    for _d8 in d8:
                                                        if _d1 != _d8 and _d2 != _d8 and _d3 != _d8 and _d4 != _d8 and _d5 != _d8 and _d6 != _d8 and _d7 != _d8 and (_d6 * 100 + (_d7 * 10) + _d8) % 11 == 0:
                                                            for _d9 in d9:
                                                                if _d1 != _d9 and _d2 != _d9 and _d3 != _d9 and _d4 != _d9 and _d5 != _d9 and _d6 != _d9 and _d7 != _d9 and _d8 != _d9 and (_d7 * 100 + (_d8 * 10) + _d9) % 13 == 0:
                                                                    for _d0 in d0:
                                                                        if _d1 != _d0 and _d2 != _d0 and _d3 != _d0 and _d4 != _d0 and _d5 != _d0 and _d6 != _d0 and _d7 != _d0 and _d8 != _d0 and (_d8 * 100 + (_d9 * 10) + _d0) % 17 == 0:
                                                                            number = str(_d1) + str(_d2) + str(_d3) + str(_d4) + str(_d5) + str(_d6) + str(_d7) + str(_d8) + str(_d9) + str(_d0)
                                                                            result += int(number)

print (result)