def is_perfect_check(number):
    positive_divisors = []
    for i in range(1, number):
        if number % i == 0:
            positive_divisors.append(i)

    return sum(positive_divisors)


number = int(input())

if is_perfect_check(number) == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")