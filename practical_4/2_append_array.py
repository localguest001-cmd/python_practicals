# Program to append element to array

import array as arr

my_array = arr.array('i', [10, 20, 30, 40, 50])

print("Original array:", my_array)

new_item = int(input("Enter a new integer: "))
my_array.append(new_item)

print("Modified array:", my_array)
