# Replace occurrences of first character

def replace_first_char(string):
    first_char = string[0]
    new_string = first_char + string[1:].replace(first_char, '$')
    return new_string

my_string = "banana"

new_string = replace_first_char(my_string)

print("Original string:", my_string)
print("Modified string:", new_string)
