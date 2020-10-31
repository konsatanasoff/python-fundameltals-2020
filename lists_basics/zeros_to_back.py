numbers = input().split(", ")

zeros = []
int_numbers = []

for el in numbers:
    el = int(el)
    int_numbers.append(el)

    if el == 0:
        zeros.append(el)
        int_numbers.remove(el)

zeros_in_back = int_numbers + zeros

print(zeros_in_back)