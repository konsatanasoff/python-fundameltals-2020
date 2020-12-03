data = input()

user_data = {}

while not data == "End":
    company, employee = data.split(" -> ")

    if company not in user_data:
        user_data[company] = [employee]
    elif company in user_data and employee not in user_data[company]:
        user_data[company].append(employee)

    data = input()

for key, value in sorted(user_data.items(), key=lambda x: x[0]):
    print(f'{key}')
    for el in value:
        print(f"-- {el}")