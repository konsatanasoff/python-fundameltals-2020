words = input().split()

word_dict = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in word_dict:
        word_dict[word_lower] = 0
    word_dict[word_lower] += 1

for (key, value) in word_dict.items():
    if not value % 2 == 0:
        print(key, end=" ")
