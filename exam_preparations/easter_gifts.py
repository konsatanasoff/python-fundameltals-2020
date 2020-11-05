def out_of_stock(gifts_list, gift):
    while gift in gifts_list:
        index = gifts_list.index(gift)
        gifts_list[index] = None
    return gifts_list


def required(gifts_list, gift, i):
    if 0 <= i < len(gifts_list):
        gifts_list[i] = gift
    return gifts_list


def just_in_case(gifts_list, gift):
    gifts_list[-1] = gift
    return gifts_list


gifts = input().split()
command = input()


while not command == "No Money":
    action, gift = command.split()[0], command.split()[1]

    if action == "OutOfStock":
        gifts = out_of_stock(gifts, gift)

    elif action == "Required":
        index = int(command.split()[2])
        if index < len(gifts):

            gifts = required(gifts, gift, index)

    elif action == "JustInCase":
        gifts = just_in_case(gifts, gift)

    command = input()

new_gifts = []
for gift in gifts:
    if gift:
        new_gifts.append(gift)
print(" ".join(new_gifts))