def isFlush(cards):
    suits = [card[1] for card in cards]
    for suit in suits:
        if (suits[0] != suit):
            return []

    cardsOrdered = [cardOrder[c[0]] for c in cards]
    return cardsOrdered 

def isRoyalFlush(cards):
    if isFlush(cards) == []:
        return False
    
    c = [card[0] for card in cards]
    hands = ['T', 'J', 'Q', 'K', 'A']
    for hand in hands:
        if hand not in c:
            return False
    return True

def isStraight(cards):
    cardsOrdered = [cardOrder[c[0]] for c in cards]
    cardsOrdered.sort()

    firstCard = cardsOrdered[0] - 1
    for card in cardsOrdered:
        if card != firstCard + 1:
            return 0
        firstCard = card

    return firstCard

def isStraightFlush(cards):
    if isFlush(cards) == []:
        return 0
    
    firstCard = isStraight(cards)
    return firstCard

def isFourOfAKind(cards):
    faces = [c[0] for c in cards]
    for c in cardOrder:
        if faces.count(c) == 4:
            return cardOrder[c]
    return 0

def isFullHouse(cards):
    faces = [c[0] for c in cards]
    for c in cardOrder:
        if faces.count(c) == 3:
            _cards = [card[0] for card in cards if card[0] != c]
            if len(_cards) == 2 and _cards[0] == _cards[1]:
                return [cardOrder[c], cardOrder[_cards[0]]]
    return []

def isThreeOfAKind(cards):
    faces = [c[0] for c in cards]
    for c in cardOrder:
        if faces.count(c) == 3:
            return cardOrder[c]
    return 0

def isOnePair(cards):
    faces = [c[0] for c in cards]
    for c in cardOrder:
        if faces.count(c) == 2:
            return cardOrder[c]
    return 0

def isTwoPairs(cards):
    faces = [c[0] for c in cards]
    for c in cardOrder:
        if faces.count(c) == 2:
            _cards = [card for card in cards if card[0] != c]
            pair = isOnePair(_cards)
            if pair > 0:
                return [cardOrder[c], pair]

    return []

def getHighestCards(cards):
    cardsOrdered = [cardOrder[c[0]] for c in cards]
    cardsOrdered.sort(reverse = True)

    return cardsOrdered

def poker(cardsA, cardsB):
    if isRoyalFlush(cardsA):
        return 'A - Royal Flush'
    elif isRoyalFlush(cardsB):
        return 'B - Royal Flush'
    straightFlushA = isStraightFlush(cardsA)
    straightFlushB = isStraightFlush(cardsB)
    if straightFlushA > straightFlushB:
        return 'A - Straight Flush ' + orderCard[straightFlushA]
    elif straightFlushA < straightFlushB:
        return 'B - Straight Flush ' + orderCard[straightFlushB]
    
    fourOfAKindA = isFourOfAKind(cardsA)
    fourOfAKindB = isFourOfAKind(cardsB)
    if fourOfAKindA > fourOfAKindB:
        return 'A - Four of a Kind ' + orderCard[fourOfAKindA]
    elif fourOfAKindA < fourOfAKindB:
        return 'B - Four of a Kind ' + orderCard[fourOfAKindB]
    
    fullHouseA = isFullHouse(cardsA)
    fullHouseB = isFullHouse(cardsB)
    if len(fullHouseA) > len(fullHouseB):
        return 'A - Full House ' + ' '.join([orderCard[p] for p in fullHouseA])
    elif len(fullHouseA) < len(fullHouseB):
        return 'B - Full House ' + ' '.join([orderCard[p] for p in fullHouseB])
    elif len(fullHouseA) > 0 and len(fullHouseB) > 0:
        if fullHouseA[0] > fullHouseB[0]:
            return 'A - Full House ' + ' '.join([orderCard[p] for p in fullHouseA])
        elif fullHouseA[0] < fullHouseB[0]:
            return 'B - Full House ' + ' '.join([orderCard[p] for p in fullHouseB])
        elif fullHouseA[1] > fullHouseB[1]:
            return 'A - Full House ' + ' '.join([orderCard[p] for p in fullHouseA])
        elif fullHouseA[1] < fullHouseB[1]:
            return 'B - Full House ' + ' '.join([orderCard[p] for p in fullHouseB])
    
    flushA = isFlush(cardsA)
    flushB = isFlush(cardsB)
    if len(flushA) > len(flushB):
        return 'A - Flush ' + ' '.join([orderCard[p] for p in flushA])
    elif len(flushA) < len(flushB):
        return 'B - Flush ' + ' '.join([orderCard[p] for p in flushB])
    elif len(flushA) == len(flushB) and len(flushA) > 0:
        if flushA[0] > flushB[0]:
            return 'A - Flush ' + ' '.join([orderCard[p] for p in flushA])
        elif flushA[0] < flushB[0]:
            return 'B - Flush ' + ' '.join([orderCard[p] for p in flushB])
        elif flushA[1] > flushB[1]:
            return 'A - Flush ' + ' '.join([orderCard[p] for p in flushA])
        elif flushA[1] < flushB[1]:
            return 'B - Flush ' + ' '.join([orderCard[p] for p in flushB])
    
    straightA = isStraight(cardsA)
    straightB = isStraight(cardsB)
    if straightA > straightB:
        return 'A - Straight ' + orderCard[straightA]
    elif straightA < straightB:
        return 'B - Straight ' + orderCard[straightB]

    threeOfAKindA = isThreeOfAKind(cardsA)
    threeOfAKindB = isThreeOfAKind(cardsB)
    if threeOfAKindA > threeOfAKindB:
        return 'A - Three of a Kind ' + orderCard[threeOfAKindA]
    elif threeOfAKindA < threeOfAKindB:
        return 'B - Three of a Kind ' + orderCard[threeOfAKindB]
    
    twoPairsA = isTwoPairs(cardsA)
    twoPairsB = isTwoPairs(cardsB)
    if twoPairsA > twoPairsB:
        return 'A - Two Pairs' + ' '.join([orderCard[p] for p in twoPairsA])
    elif twoPairsA < twoPairsB:
        return 'B - Two Pairs ' + ' '.join([orderCard[p] for p in twoPairsB])

    pairA = isOnePair(cardsA)
    pairB = isOnePair(cardsB)
    if pairA > pairB:
        return 'A - One Pair of ' + orderCard[pairA]
    elif pairA < pairB:
        return 'B - One Pair of ' + orderCard[pairB]
    else:
        _cardsA = getHighestCards(cardsA)
        _cardsB = getHighestCards(cardsB)
        for cardA in _cardsA:
            for cardB in _cardsB:
                if cardA > cardB:
                    return 'A - Highest Card ' + orderCard[cardA]
                elif cardA < cardB:
                    return 'B - Highest Card ' + orderCard[cardB]
        return ''
    

cardOrder = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
    'A': 13
}
orderCard = dict((cardOrder[k], k) for k in cardOrder)

file1 = open('p054_poker.txt', 'r')
result = 0

games = [g.strip() for g in file1.read().split('\n') if len(g.strip()) > 0]
file1.close()

for game in games:
    cards = game.split(' ')
    cardsA = cards[0:5]
    cardsB = cards[5:]
    state = poker(cardsA, cardsB)
    print (cardsA, ' *** ', cardsB, ' = ', state)
    if state.startswith('A - '):
        result += 1

print (result)
