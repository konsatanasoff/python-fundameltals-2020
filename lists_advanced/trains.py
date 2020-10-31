wagons = int(input())

train = [0] * wagons

command = input()
while not command == "End":
    split_command = command.split()

    if split_command[0] == "add":
        people = int(split_command[1])
        train[-1] += people
    elif split_command[0] == "insert":
        index = int(split_command[1])
        people = int(split_command[2])
        train[index] += people
    elif split_command[0] == "leave":
        index = int(split_command[1])
        people = int(split_command[2])
        train[index] -= people

    command = input()

print(train)