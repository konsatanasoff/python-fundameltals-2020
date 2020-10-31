n = int(input())
word = input()
words = []
match_words = []

for i in range(n):
    current_word = input()
    words.append(current_word)
    if word in current_word:
        match_words.append(current_word)

print(words)
print(match_words)
