text = input()
reps = int(input())


def repeat_string(string, rep):
    result = ''
    for i in range(0, rep):
        result += string
    return result


print(repeat_string(text, reps))