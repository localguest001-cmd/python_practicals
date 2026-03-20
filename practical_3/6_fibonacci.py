# Program to print Fibonacci series

n = int(input("Enter the number of terms: "))

first_term = 0
second_term = 1

print("Fibonacci series:")
print(first_term)
print(second_term)

for i in range(2, n):
    next_term = first_term + second_term
    print(next_term)
    first_term = second_term
    second_term = next_term
