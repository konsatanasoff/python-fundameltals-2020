def add(pieces, piece, composer, key):
    if piece not in pieces:
        pieces[piece] = {'composer': composer, 'key': key}
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")
    return pieces


def remove(pieces, piece):
    if piece in pieces:
        del pieces[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return pieces


def change_key(pieces, piece, key):
    if piece in pieces:
        pieces[piece]['key'] = key
        print(f"Changed the key of {piece} to {key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return pieces


n_pieces = int(input())

pieces = {}

for _ in range(n_pieces):
    piece, composer, key = input().split("|")
    pieces[piece] = {'composer': composer, 'key': key}

command = input()

while not command == "Stop":
    action = command.split("|")[0]

    if action == "Add":
        piece, composer, key = command.split("|")[1:]
        pieces = add(pieces, piece, composer, key)
    elif action == "Remove":
        piece = command.split("|")[1]
        pieces = remove(pieces, piece)
    elif action == "ChangeKey":
        piece, new_key = command.split("|")[1:]
        pieces = change_key(pieces, piece, new_key)

    command = input()

pieces = dict(sorted(pieces.items(), key=lambda x: (x[0], x[1]['composer'])))

for piece in pieces:
    print(f"{piece} -> Composer: {pieces[piece]['composer']}, Key: {pieces[piece]['key']}")
