people_waiting = int(input())
lift = list(map(int, input().split()))
MAX_SEATS_PER_WAGON = 4


for index in range(len(lift)):
    while not lift[index] == MAX_SEATS_PER_WAGON:
        if people_waiting > 0:
            lift[index] += 1
            people_waiting -= 1
        else:
            break

all_seats = len(lift) * MAX_SEATS_PER_WAGON
if people_waiting == 0 and (sum(lift) < all_seats):
    print(f"The lift has empty spots!")
elif people_waiting > 0 and (sum(lift) == all_seats):
    print(f"There isn't enough space! {people_waiting} people in a queue!")
print(" ".join(map(str, lift)))