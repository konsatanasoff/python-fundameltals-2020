first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
student_count = int(input())

all_employees = first_employee + second_employee + third_employee
hours = 0

while not student_count <= 0:
    hours += 1
    student_count -= all_employees
    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")