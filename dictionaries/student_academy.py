n_rows = int(input())

students = {}

for _ in range(n_rows):
    student = input()
    grade = float(input())

    if student not in students:
        students[student] = [grade]
    else:
        students[student].append(grade)

for student, average_grade in students.items():
    students[student] = sum(average_grade) / len(average_grade)

ordered_students = sorted(students.items(), key=lambda s: s[1], reverse=True)

for student, average_grade in ordered_students:
    if average_grade >= 4.5:
        print(f'{student} -> {average_grade:.2f}')