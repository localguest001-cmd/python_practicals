# Program to count character frequency

my_string = "{{NAME}}"

char_freq = {}

for char in my_string:
    if char not in char_freq:
        char_freq[char] = 1
    else:
        char_freq[char] += 1

for char in char_freq:
    print(char, ":", char_freq[char])
