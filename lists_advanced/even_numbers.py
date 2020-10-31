numbers = list(map(lambda x: int(x), input().split(", ")))
even_indices = []

for el in range(len(numbers)):
    if numbers[el] % 2 == 0:
        even_indices.append(el)

print(even_indices)