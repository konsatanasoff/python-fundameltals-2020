import time


def convert(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))


leave_time = input()
n_steps = int(input())
step_seconds = int(input())

hh, mm, ss = leave_time.split(":")
total_seconds = (int(hh) * 3600 + int(mm) * 60 + int(ss)) + step_seconds * n_steps

print(f"Time Arrival: {convert(total_seconds)}")
