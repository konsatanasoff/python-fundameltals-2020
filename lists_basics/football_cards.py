import re

cards = input()

a_team = 11
b_team = 11

a_cards = []
b_cards = []

split_cards = re.split("- |, |", cards)
split_cards = list(filter(None, split_cards))


for iteration in split_cards:
    if iteration == "A":
        a_team -= 1
    if iteration == "B":
        b_team -= 1

    if a_team < 7 or b_team < 7:
        break

print(f"Team A - {a_team}; Team B - {b_team}")

if a_team < 7 or b_team < 7:
    print("Game was terminated")