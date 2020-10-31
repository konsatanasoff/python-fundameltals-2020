version = input().split(".")

new = int("".join(version))

new_version = int(new + 1)

print(".".join(str(new_version)))
