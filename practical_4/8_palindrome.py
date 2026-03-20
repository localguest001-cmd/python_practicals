# Check palindrome

def is_palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False

string = "{{NAME}}"

if is_palindrome(string):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
