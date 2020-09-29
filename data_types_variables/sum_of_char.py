n_lines = int(input())

sum_letters = 0

for i in range(1, n_lines + 1):
    letters = input()
    sum_letters += ord(letters)

print(f"The sum equals: {sum_letters}")