import re


def has_numbers(string):
    return any(char.isdigit() for char in string)


def num_sum(string):
    numbers = ''
    for i in string:
        if i.isdigit():
            numbers += i
    return numbers


def is_capital(data):
    first_letter = data[0]
    last_letter = data[-1]
    if first_letter.isupper() and last_letter.isupper():
        return True
    else:
        return False


pattern = r"@#+(?P<barcode>[a-zA-Z0-9]{6,})@#+"

n_count = int(input())

for _ in range(n_count):
    data = input()
    if re.findall(pattern, data) and is_capital(re.findall(pattern, data)[0]):
        for el in re.finditer(pattern, data):
            barcode = el[1]
            if has_numbers(barcode):
                digits = num_sum(barcode)
                print(f"Product group: {digits}")
            else:
                print("Product group: 00")
    else:
        print("Invalid barcode")

