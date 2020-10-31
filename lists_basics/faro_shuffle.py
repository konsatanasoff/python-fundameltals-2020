cards = input().split()
n_splits = int(input())

first_card = cards[0]
last_card = cards[-1]

half = len(cards) // 2

shuffled_cards = []

for split in range(n_splits):
    left_cards = []
    right_cards = []

    for index in range(1, half):
        left_cards.append(cards[index])

    for index in range(half, len(cards) - 1):
        right_cards.append(cards[index])

    for index in range(len(left_cards)):
        shuffled_cards.append(right_cards[index])
        shuffled_cards.append(left_cards[index])

    cards = shuffled_cards.copy()
    cards.append(last_card)
    cards.insert(0, first_card)
    shuffled_cards = []

print(cards)