# Find repeated items in tuple

my_tuple = (1, 2, 3, 4, 3, 5, 2)

repeated_items = []

for item in my_tuple:
    if my_tuple.count(item) > 1 and item not in repeated_items:
        repeated_items.append(item)

print("The repeated items in the tuple are:", repeated_items)
