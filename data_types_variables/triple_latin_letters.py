n = int(input())

ascii_letter = ord('a')
for first_char in range(ascii_letter, ascii_letter + n):
    for second_char in range(ascii_letter, ascii_letter + n):
        for third_char in range(ascii_letter, ascii_letter + n):

            print(f"{chr(first_char)}"
                  f"{chr(second_char)}"
                  f"{chr(third_char)}")
