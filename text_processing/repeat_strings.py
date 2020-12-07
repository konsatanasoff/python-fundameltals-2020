line = input().split()

for el in line:
    print(f"{el * len(el)}", end="")
