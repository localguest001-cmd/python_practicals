# Function to sum elements of list

def sum_list(a):
    total = 0
    for i in a:
        total += i
    return total

l = [1, 2, 4, 5]

print("Sum is:", sum_list(l))
