student_count = int(input())
lecture_count = int(input())
initial_bonus = int(input())

max_bonus = 0
max_lectures = 0

for attendance in range(student_count):
    attendance_count = int(input())
    total_bonus = attendance_count / lecture_count * (5 + initial_bonus)
    if total_bonus >= max_bonus:
        max_bonus = total_bonus
        max_lectures = attendance_count

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {max_lectures} lectures.")
