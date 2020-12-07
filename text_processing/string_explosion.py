line = input().split(">")
explosion_str = 0
after_explosion = []

for el in line:
    if el[0].isdigit():
        explosion_str += int(el[0])
        if len(el) <= explosion_str:
            explosion_str -= len(el)
            el = ">"
        else:
            el = ">"+"".join(list(el[explosion_str::]))
            explosion_str = 0

    after_explosion.append(el)

print(''.join(after_explosion))

