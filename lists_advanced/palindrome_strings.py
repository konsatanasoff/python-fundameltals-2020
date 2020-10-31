strings = input().split(" ")
search_word = input()

palindromes = []

for word in strings:
    if word == word[::-1]:
        palindromes.append(word)

print(f"{palindromes}")
print(f"Found palindrome {palindromes.count(search_word)} times")