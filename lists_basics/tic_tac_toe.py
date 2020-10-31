row_1 = input().split(" ")
row_2 = input().split(" ")
row_3 = input().split(" ")

player_1_win = False
player_2_win = False
draw = False

for i in row_1:
    i = int(i)
    for j in row_2:
        j = int(j)
        for k in row_3:
            k = int(k)

            if row_1[i] == 1 and row_2[j] == 1 and row_3[k] == 1:
                player_1_win = True
            elif row_1[i] == 2 and row_2[j] == 2 and row_3[k] == 2:
                player_2_win = True

if player_1_win:
    print("First player won")
elif player_2_win:
    print("Second player won")
else:
    print("Draw!")


a = 5