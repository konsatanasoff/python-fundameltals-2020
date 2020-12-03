def add_user(forces_dict, given_side, given_user):
    for side, users in forces_dict.items():
        if given_user in users:
            return forces_dict
    if given_side not in forces_dict:
        forces_dict[given_side] = []
        forces_dict[given_side].append(given_user)
    else:
        if given_user not in forces_dict[given_side]:
            forces_dict[given_side].append(given_user)
    return forces_dict


def transfer_user(forces_dict, given_side, given_user):
    for side, users in forces_dict.items():
        if given_user in users:
            forces_dict[side].remove(given_user)
            return add_user(forces_dict, given_side, given_user)
    return add_user(forces_dict, given_side, given_user)


command = input()

forces = {}

while not command == "Lumpawaroo":

    if "->" in command:
        user, side = command.split(" -> ")
        forces = transfer_user(forces, side, user)
        print(f"{user} joins the {side} side!")
    elif "|" in command:
        side, user = command.split(" | ")
        forces = add_user(forces, side, user)

    command = input()

ordered_forces = sorted(forces.items(), key=lambda x: (-len(x[1]), x[0]))

for side, users in ordered_forces:
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in sorted(users):
            print(f"! {user}")