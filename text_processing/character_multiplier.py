data = input().split()
result = 0

data.sort(key=lambda x: len(x))

for char in range(len(data[0])):
    result += ord(data[0][char]) * ord(data[1][char])

remaining = sum([ord(i) for i in data[1][len(data[0]):]])
result += remaining

print(result)