gifts = input().split()
command = input()
out_of_stock = "OutOfStock"
required = "Required"
just_in_case = "JustInCase"


gifts_list = []
for i in gifts:
    gifts_list.append(i)

while command != "No Money":
    text = command.split()
    if out_of_stock in text:
        for i in range(len(gifts_list)):
            if text[1] in gifts_list:
                index = gifts_list.index(text[1])
                gifts_list[index] = None
    elif required in text:
        index = int(text[2])
        if len(gifts_list) > index >= 0:
            gifts_list[index] = text[1]
    else:
         if just_in_case in text:
             for i in range (len(gifts_list)):
                 gifts_list[-1] = text[1]

    command = input()

while None in gifts_list:
    gifts_list.remove(None)
for i in gifts_list:
    print(i, end= " ")