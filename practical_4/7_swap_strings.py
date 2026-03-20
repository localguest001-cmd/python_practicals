# Swap first two characters of strings

def swap_first_two(string1, string2):
    new_string1 = string2[:2] + string1[2:]
    new_string2 = string1[:2] + string2[2:]
    result = new_string1 + ' ' + new_string2
    return result

string1 = "{{NAME}}"
string2 = "Cloud"

result = swap_first_two(string1, string2)

print(result)
