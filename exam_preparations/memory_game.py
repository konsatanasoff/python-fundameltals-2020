sequence = input().split()

command = input()
count = 0


def index_remove(my_list, first, second):
    indexes = [first, second]
    for index in sorted(indexes, reverse=True):
        del my_list[index]
    return my_list


while not command == "end":
    first_element, second_element = command.split()
    first_element = int(first_element)
    second_element = int(second_element)
    count += 1

    if first_element == second_element or first_element not in range(len(sequence)) or second_element not in range(len(sequence)):
        sequence.insert((len(sequence) // 2), f"-{count}a")
        sequence.insert((len(sequence) // 2) + 1, f"-{count}a")
        print(f"Invalid input! Adding additional elements to the board")

    elif sequence[first_element] == sequence[second_element]:
        print(f"Congrats! You have found matching elements - {sequence[first_element]}!")
        sequence = index_remove(sequence, first_element, second_element)

        if len(sequence) == 0:
            print(f"You have won in {count} turns!")
            break

    else:
        print(f"Try again!")

    command = input()

if len(sequence) > 0:
    print(f"Sorry you lose :(")
    print(" ".join(map(str, sequence)))
