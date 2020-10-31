nums = input()
numbers = []

for i in nums.split():
    if int(i) >= 0:
        numbers.append(int(i) * - 1)
    elif int(i) < 0:
        numbers.append(abs(int(i)))

print(numbers)