numbers = input().split()
n_remove = int(input())

numbers = [int(i) for i in numbers]

for iteration in range(n_remove):
    numbers.remove(min(numbers))

print(numbers)