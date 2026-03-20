# Function to print even numbers

def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

list1 = [22, 5, 2003]

print("Even items are:", even_numbers(list1))
