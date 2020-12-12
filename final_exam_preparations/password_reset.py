def take_odd(old_pass):
    new_pass = ''
    for i in range(len(old_pass)):
        if not i % 2 == 0:
            new_pass += old_pass[i]
    print(new_pass)
    return new_pass


def cut(old_pass, i, len):
    left_side = old_pass[:i]
    right_side = old_pass[i + len:]
    new_pass = left_side + right_side
    print(new_pass)
    return new_pass


def substitute(old_pass, substring, to_sub):
    if substring in old_pass:
        old_pass = old_pass.replace(substring, to_sub)
        print(old_pass)
    else:
        print(f"Nothing to replace!")
    return old_pass


old_password = input()
data = input()

while not data == "Done":

    if "TakeOdd" in data:
        old_password = take_odd(old_password)

    elif "Cut" in data:
        command, index, length = data.split()
        index = int(index)
        length = int(length)
        old_password = cut(old_password, index, length)

    elif "Substitute" in data:
        substring = data.split()[1]
        to_substitute = data.split()[2]
        old_password = substitute(old_password, substring, to_substitute)

    data = input()

print(f"Your password is: {old_password}")