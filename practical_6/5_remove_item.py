# Remove item from tuple

my_tuple = (1, 2, 3, 4, 5)
item_to_remove = 3

new_tuple = tuple(item for item in my_tuple if item != item_to_remove)

print("The new tuple is:", new_tuple)
