f = open("54_poker.txt", "r")
hands = []
for line in f:
    hands.append([ele for ele in line.strip(" \n\t").split(" ")])
f.close()


def hand_evaluator(hand):
    value_thesaurus = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    value_list = []
    value_dict = {}
    suits = {"D": 0, "H": 0, "S": 0, "C": 0}
    pairs = [0, []]
    three_kind = 0
    four_kind = 0
    straight = 0
    flush = []

    for card in hand:
        value, suit = card[0], card[1]
        if value in value_thesaurus:
            if value_thesaurus[value] in value_dict:
                value_dict[value_thesaurus[value]] += 1
            else:
                value_dict[value_thesaurus[value]] = 1
            value_list.append(value_thesaurus[value])
        else:
            if int(value) in value_dict:
                value_dict[int(value)] += 1
            else:
                value_dict[int(value)] = 1
            value_list.append(int(value))
        suits[suit] += 1

    for value, count in value_dict.items():
        if count == 2:
            pairs[0] += 1
            pairs[1].append(value)
        if count == 3:
            three_kind = value
        if count == 4:
            four_kind = value

    value_list.sort()

    if len(set(value_list)) == len(value_list):
        if value_list[-1] - value_list[0] == 4:
            straight = value_list[-1]
        elif value_list[-1] == 14 and value_list[-2] == 5:
            straight = value_list[-2]

    for count in suits.values():
        if count == 5:
            flush = value_list
        elif count > 0:
            break

    if flush and straight:
        return (8, straight)
    if four_kind:
        return (7, four_kind)
    if pairs[0] and three_kind:
        return (6, three_kind)
    if flush:
        return (5, flush)
    if straight:
        return (4, straight)
    if three_kind:
        return (3, three_kind)
    if pairs[0] == 2:
        ret = set(value_list)
        for val in pairs[1]:
            ret.remove(val)
        return (pairs[0], sorted(pairs[1]), ret.pop())
    if pairs[0] == 1:
        ret = set(value_list)
        for val in pairs[1]:
            ret.remove(val)
        return (pairs[0], pairs[1], sorted(list(ret)))
    return (0, value_list)


def winner(player_one, player_two):
    if player_one[0] > player_two[0]:
        return 1

    if player_one[0] < player_two[0]:
        return 0

    if player_one[0] == player_two[0]:

        if player_one[0] == 2:
            for idx in range(1, -1, -1):
                if player_one[1][idx] > player_two[1][idx]:
                    return 1
                if player_one[1][idx] < player_two[1][idx]:
                    return 0
            if player_one[2] > player_two[2]:
                return 1
            if player_one[2] < player_two[2]:
                return 0

        if player_one[0] == 1:
            if player_one[1] > player_two[1]:
                return 1
            if player_one[1] < player_two[1]:
                return 0
            for idx in range(2, -1, -1):
                if player_one[2][idx] > player_two[2][idx]:
                    return 1
                if player_one[2][idx] < player_two[2][idx]:
                    return 0

        if player_one[0] == 5 or player_one[0] == 0:
            for idx in range(4, -1, -1):
                if player_one[1][idx] > player_two[1][idx]:
                    return 1
                if player_one[1][idx] < player_two[1][idx]:
                    return 0

        if player_one[1] > player_two[1]:
            return 1
        return 0


player_one_wins = 0
for hand in hands:
    player_one, player_two = hand_evaluator(hand[0:5]), hand_evaluator(hand[5:10])
    player_one_wins += winner(player_one, player_two)
print(player_one_wins)
