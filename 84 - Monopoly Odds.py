import random

def format(number):
    if number < 10:
        return '0' + str(number)
    return str(number)

board = [0] * 40
SIDES = 4
SAMPLES = 1000000
doubles = 0
position = 0
chance_position = 0
community_position = 0

for i in range(0, SAMPLES):
    dice1 = random.randint(1, SIDES)
    dice2 = random.randint(1, SIDES)
    if dice1 == dice2:
        doubles += 1
        if doubles > 2:
            position = 10
            doubles = 0
    else:
        position = (position + dice1 + dice2) % len(board)
        doubles = 0
        #chance
        if position == 7 or position == 22 or position == 36:
            chance = [0, 10, 11, 24, 39, 5]
            chance_position = (chance_position + 1) % 16
        
            if chance_position < 6:
                position = chance[chance_position]
        
            if chance_position == 6 or chance_position == 7:
                if position == 7:
                    position = 15
                if position == 22:
                    position = 25
                if position == 36:
                    position = 5
        
            if chance_position == 8:
                if position == 22:
                    position = 28
                else:
                    position = 12
        
            if chance_position == 9:
                position -= 3
        #community
        if position == 2 or position == 17 or position == 33:
            cc = [0, 10]
            community_position = (community_position + 1) % 16
        
            if community_position < 2:
                position = cc[community_position]
        if position == 30:
            position = 10
        
        board[position] += 1

results = [ [x, board[x]] for x in range(0, len(board))]
results.sort(key=lambda x: -x[1])
print (results)
print (format(results[0][0]) + format(results[1][0]) + format(results[2][0]))