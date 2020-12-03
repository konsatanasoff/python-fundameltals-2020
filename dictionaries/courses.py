command = input()

course_data = {}

while not command == "end":
    data = command.split(" : ")
    course = data[0]
    student = data[1]

    if course not in course_data:
        course_data[course] = []
    course_data[course].append(student)

    command = input()

for key, value in sorted(course_data.items(), key=lambda x: -len(x[1])):
    print(f'{key}: {len(value)}')
    for el in sorted(value):
        print(f"-- {el}")
