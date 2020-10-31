first_list = input().split(", ")
second_list = input().split(", ")
are_in = []

for element in first_list:
    for el in second_list:
        if element in el:
            if not element in are_in:
                are_in.append(element)

print(are_in)