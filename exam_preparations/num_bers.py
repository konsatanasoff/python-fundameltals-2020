numbers = list(map(int, input().split()))
average = sum(numbers) / len(numbers)

grater = []

for number in sorted(numbers, reverse=True):
    if number > average:
        grater.append(number)

if len(grater) > 0:
    print(" ".join(map(str, grater[:5])))
else:
    print("No")


