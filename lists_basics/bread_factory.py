events = input().split("|")

total_energy = 100
coins = 100
day_end = False

for el in events:
    event, event_value = el.split("-")
    event_value = int(event_value)

    if event == "rest":

        if (total_energy + event_value) > 100:
            total_energy = 100
            print("You gained 0 energy.")
            print(f"Current energy: 100.")

        else:
            total_energy += event_value
            print(f"You gained {event_value} energy.")
            print(f"Current energy: {total_energy}.")

    elif event == "order":

        if total_energy >= 30:
            total_energy -= 30
            coins += event_value
            print(f"You earned {event_value} coins.")

        else:
            print(f"You had to rest!")
            total_energy += 50

    elif not event == "rest" and not event == "order":

        coins -= event_value

        if coins <= 0:
            day_end = True
            break
        else:
            print(f"You bought {event}.")

if not day_end:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {total_energy}")
elif day_end:
    print(f"Closed! Cannot afford {event}.")