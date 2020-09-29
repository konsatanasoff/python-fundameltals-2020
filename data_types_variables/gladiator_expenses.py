lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_cost = 0
shield_break_count = 0

for fight in range(1, lost_fight_count + 1):
    if fight % 2 == 0:
        total_cost += helmet_price
    if fight % 3 == 0:
        total_cost += sword_price

    if fight % 2 == 0 and fight % 3 == 0:
        total_cost += shield_price
        shield_break_count += 1
        if shield_break_count == 2:
            total_cost += armor_price
            shield_break_count = 0

print(f"Gladiator expenses: {total_cost:.2f} aureus")