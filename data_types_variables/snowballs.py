import sys
n_snowballs = int(input())

highest_ball_snow = 0
highest_ball_time = 0
highest_ball_quality = 0
highest_ball_value = -sys.maxsize

for i in range(1, n_snowballs + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_snow / snowball_time) ** snowball_quality

    if snowball_value > highest_ball_value:
        highest_ball_value = snowball_value
        highest_ball_snow = snowball_snow
        highest_ball_time = snowball_time
        highest_ball_quality = snowball_quality

print(f"{highest_ball_snow} : {highest_ball_time} = {int(highest_ball_value)} ({highest_ball_quality})")
