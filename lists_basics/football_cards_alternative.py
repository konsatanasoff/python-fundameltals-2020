received_cards = input()

cards_list = received_cards.split()

a_cards = []
b_cards = []

a_team = 11
b_team = 11

is_terminated = False

for item in range(len(cards_list)):
    if cards_list[item][0] == "A":
        if cards_list[item] in a_cards:
            pass
        else:
            a_cards.append(cards_list[item])
            a_team -= 1

    if cards_list[item][0] == "B":
        if cards_list[item] in b_cards:
            pass
        else:
            b_cards.append(cards_list[item])
            b_team -= 1

    if a_team < 7 or b_team < 7:
        is_terminated = True
        break

print(f"Team A - {a_team}; Team B - {b_team}")

if is_terminated:
    print(f"Game was terminated")