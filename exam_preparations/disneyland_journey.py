journey_cost = int(input())
n_months = int(input())

saved_money = 0

for month in range(1, n_months + 1):

    if month % 2 == 1 and not month == 1:
        saved_money -= saved_money * 0.16

    if month % 4 == 0:
        saved_money += saved_money * 0.25

    saved_money += journey_cost * 0.25


souvenirs = saved_money - journey_cost

if saved_money > journey_cost:
    print(f"Bravo! You can go to Disneyland and you will have {souvenirs:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {abs(souvenirs):.2f}lv. more.")