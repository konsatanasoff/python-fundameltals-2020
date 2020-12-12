import re


pattern_emoji = r"(::|\*\*)(?P<emoji>[A-Z][a-z]{2,})\1"
digit_pattern = r"\d+"

string = input()
cool_threshold = 1
cool_emojis = []
valid_emojis = [el.group() for el in re.finditer(pattern_emoji, string)]

for d in re.findall(digit_pattern, string):
    num = [el for el in d]
    for n in num:
        cool_threshold *= int(n)

for emoji in re.findall(pattern_emoji, string):
    coolness = sum([ord(char) for char in emoji[1]])
    if coolness >= cool_threshold:
        cool_emojis.append(emoji[0] + emoji[1] + emoji[0])

print(f"Cool threshold: {cool_threshold}")
print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:")
for moji in cool_emojis:
    print(moji)

