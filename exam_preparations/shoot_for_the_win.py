targets = list(map(int, input().split()))
to_shoot = input()

while not to_shoot == "End":
    index = int(to_shoot)

    if index < len(targets):
        shooting_index = targets[index]
        targets.pop(index)

        for i in range(len(targets)):

            if targets[i] > shooting_index:
                targets[i] -= shooting_index

            elif not targets[i] == -1:
                targets[i] += shooting_index

        targets.insert(index, -1)

    to_shoot = input()

print(f"Shot targets: {len([_ for _ in targets if _ == -1])} -> {' '.join(list(map(str, targets)))}")
