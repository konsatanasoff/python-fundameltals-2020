from math import ceil

num_list = input().split(", ")
int_numbers = list(map(int, num_list))

for i in range(1, ceil(max(int_numbers) / 10) + 1):
    result = []

    for j in range(len(int_numbers)):

        if int_numbers[j] in range(i * 10 - 10 + 1, i * 10 + 1):
            result.append(int_numbers[j])

    print(f"Group of {i * 10}'s: {result}")
