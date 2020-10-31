n = int(input())

count_positive = []
count_negative = []

for i in range(n):
    num = int(input())

    if num > 0:
        count_positive.append(num)
    else:
        count_negative.append(num)

print(count_positive)
print(count_negative)

print(f"Count of positives: {len(count_positive)}. "
      f"Sum of negatives: {sum(count_negative)}")