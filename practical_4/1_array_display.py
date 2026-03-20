# Program to display array elements

import array as arr

my_array = arr.array('i', [10, 20, 30, 40, 50])

print("Array items:")
for item in my_array:
    print(item)

print("Element at index 0:", my_array[0])
print("Element at index 2:", my_array[2])
print("Element at index 4:", my_array[4])
