HIGH_FIRE_TYPE = range(81, 126)
MEDIUM_FIRE_TYPE = range(51, 81)
LOW_FIRE_TYPE = range(1, 51)

fires = input().split("#")
total_water = int(input())

total_effort = 0
total_fire = 0
fires_put_out = []

for fire in fires:
    fire_type, value = fire.split(" = ")
    value = int(value)

    if fire_type == "High" and value not in HIGH_FIRE_TYPE:
        continue
    elif fire_type == "Medium" and value not in MEDIUM_FIRE_TYPE:
        continue
    elif fire_type == "Low" and value not in LOW_FIRE_TYPE:
        continue

    if value <= total_water:
        total_water -= value
        total_fire += value
        total_effort += value * 0.25
        fires_put_out.append(value)

    elif value > total_water:
        continue

print("Cells:")

for fire in fires_put_out:
    print(f" - {fire}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
