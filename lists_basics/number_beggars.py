number = input()
n_beggars = int(input())

split_numbers = number.split(", ")
beggars = []

for i in range(n_beggars):
    beggars.append(0)
i = 0

while len(split_numbers) > 0:
    split_numbers[0] = int(split_numbers[0])
    if i < len(beggars):
        beggars[i] += split_numbers[0]
    else:
        i = 0
        continue
    split_numbers.pop(0)
    i += 1

print(beggars)

