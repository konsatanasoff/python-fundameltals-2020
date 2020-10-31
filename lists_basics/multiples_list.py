factor = int(input())
count = int(input())

final_list = []

for iteration in range(1, count + 1):
    iteration *= factor
    final_list.append(iteration)

print(final_list)