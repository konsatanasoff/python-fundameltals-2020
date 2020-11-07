from math import ceil

budget = float(input())
students = int(input())
price_flour = float(input())
price_egg = float(input())
price_apron = float(input())


total_sets_price = 0
flour_count = 0

for student in range(1, students + 1):
    if student % 5 == 0:
        flour_count += 1

total_apron_price = price_apron * ceil(students * 1.20)
total_egg_price = (price_egg * 10) * students
total_flour_price = price_flour * (students - flour_count)
total_sets_price = total_flour_price + total_egg_price + total_apron_price


if budget >= total_sets_price:
    print(f"Items purchased for {total_sets_price:.2f}$.")
else:
    print(f"{total_sets_price - budget:.2f}$ more needed.")

