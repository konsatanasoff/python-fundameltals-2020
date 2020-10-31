def even_odd_separator():
    number_digits = [int(d) for d in received_number]
    even_sum = 0
    odd_sum = 0

    for num in number_digits:
        if num % 2 == 0:
            even_sum += num
        elif num % 2 == 1:
            odd_sum += num

    return even_sum, odd_sum


received_number = input()

even, odd = even_odd_separator()

print(f"Odd sum = {odd}, Even sum = {even}")