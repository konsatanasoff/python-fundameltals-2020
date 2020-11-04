first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
people = int(input())

total_per_employee = first_employee + second_employee + third_employee
hours = 0

while people > 0:

    people -= total_per_employee
    hours += 1
    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")