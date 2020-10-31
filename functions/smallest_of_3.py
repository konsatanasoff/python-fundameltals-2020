first_num = int(input())
second_num = int(input())
third_num = int(input())


def smallest_check():
    all_nums = [first_num, second_num, third_num]
    result = min(all_nums)
    return result


print(smallest_check())