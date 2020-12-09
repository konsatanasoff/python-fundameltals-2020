import re

pattern = r"[0-9]+"

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

sequence = '\n'.join(lines)

nums = re.findall(pattern, sequence)

for num in nums:
    print(num, end=' ')

