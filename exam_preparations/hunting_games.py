n_days = int(input())
player_count = int(input())
group_energy = float(input())
water = float(input())
food = float(input())

needed_water = n_days * player_count * water
needed_food = n_days * player_count * food


for day in range(1, n_days + 1):
    energy_loss = float(input())
    group_energy -= energy_loss

    if group_energy <= 0:
        break

    if day % 2 == 0:
        group_energy *= 1.05
        needed_water *= 0.70

    if day % 3 == 0:
        needed_food -= needed_food / player_count
        group_energy *= 1.10

if group_energy > 0:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")

else:
    print(f"You will run out of energy. You will be left with {needed_food:.2f} food and {needed_water:.2f} water.")