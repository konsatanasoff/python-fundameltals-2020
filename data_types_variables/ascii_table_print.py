start = int(input())
end = int(input())

sum = ""

for i in range(start, end + 1):
    sum += chr(i) + " "

print(sum, end=' ')
