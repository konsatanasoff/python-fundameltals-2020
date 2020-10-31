numbers = list(map(int, input().split(" ")))


def exchange(i):
    global numbers # benutzen die erste "numbers"
    if i < 0 or i >= len(numbers):
        print("Invalid index")
        return  # oder else
    numbers = numbers[i+1:] + numbers[:i+1]


def max_even_odd(command):
    global numbers

    if command == "even":
        if len([x for x in numbers if x % 2 == 0]) == 0:
            print("No matches")
            return
        num = [x for x in numbers if x % 2 == 0] [0]
    else:
        if len([x for x in numbers if x % 2 != 0]) == 0:
            print("No matches")
            return
        num = [x for x in numbers if x % 2 != 0][0]
    index = 0
    for i in range (len(numbers)):
        current = numbers[i]
        if command == "even":
            if current >= num and current % 2 == 0:
                num = current
                index = i
        else:
            if current >= num and current % 2 != 0:
                num = current
                index = i
    print(index)


def min_even_odd(command):
    global numbers

    if command == "even":
        if len([x for x in numbers if x % 2 == 0]) == 0:
            print("No matches")
            return
        num = [x for x in numbers if x % 2 == 0] [0]
    else:
        if len([x for x in numbers if x % 2 != 0]) == 0:
            print("No matches")
            return
        num = [x for x in numbers if x % 2 != 0][0]
    index = 0

    for i in range(len(numbers)):
        current = numbers[i]
        if command == "even":
            if current <= num and current % 2 == 0:
                num = current
                index = i
        else:
            if current <= num and current % 2 != 0:
                num = current
                index = i
    print(index)


def first_odd_even(count,command):
    global numbers

    result = []
    if count > len(numbers):
        print("Invalid count")
        return

    for i in numbers:
        if len(result) == count:
            break
        if command == "even":
            if i % 2 == 0:
                result.append(i)
        else:
            if i % 2 != 0:
                result.append(i)

    print(result)


def last_odd_even(count, command):
    global numbers

    result = []
    if count > len(numbers):
        print("Invalid count")
        return
    reversed_numbers = list(reversed(numbers)) # ohne [rev_num] das send nur das Resultat,ohne das zu speichern.
    for i in reversed_numbers:
        if len(result) == count:
            break
        if command == "even":
            if i % 2 == 0:
                result.append(i)
        else:
            if i % 2 != 0:
                result.append(i)

    print(list(reversed(result)))


command = input()

while not command == "end":
    text = command.split()
    if text[0] == "exchange":
        i = int(text[1])
        exchange(i)
    elif text[0] == "max":
        max_even_odd(text[1])
    elif text[0] == "min":
        min_even_odd(text[1])
    elif text[0] == "first":
        count = int(text[1])
        first_odd_even(count,text[2])
    elif text[0] == "last":
        count = int(text[1])
        last_odd_even(count,text[2])

    command = input()

print(numbers)