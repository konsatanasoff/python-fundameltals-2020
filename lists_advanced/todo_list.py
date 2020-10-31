command = input()

todo_list = [0] * 10

while not command == "End":
    importance, note = command.split("-")
    importance = int(importance)

    todo_list.insert(importance, note)
    todo_list.remove(0)
    command = input()

result = []
for el in todo_list:
    if not el == 0:
        result.append(el)

print(result)