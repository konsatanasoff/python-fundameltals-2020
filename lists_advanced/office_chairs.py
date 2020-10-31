rooms = int(input())

free_chairs = 0
room_counter = 0
needed_chairs = 0

for _ in range(1, rooms + 1):
    total_chairs, taken_chairs = input().split()
    room_counter += 1

    if len(total_chairs) >= int(taken_chairs):
        free_chairs += (len(total_chairs) - int(taken_chairs))

    elif len(total_chairs) < int(taken_chairs):
        needed_chairs_in_room = int(taken_chairs) - len(total_chairs)
        needed_chairs += needed_chairs_in_room
        print(f"{needed_chairs_in_room} more chairs needed in room {room_counter}")

if free_chairs >= needed_chairs:
    free_chairs -= needed_chairs
    print(f"Game On, {free_chairs} free chairs left")