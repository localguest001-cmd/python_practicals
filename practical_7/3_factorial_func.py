# Function to calculate factorial

def fact(num):
    if num < 0:
        return "Factorial not defined for negative numbers"
    elif num == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        return factorial

n = int(input("Enter a number: "))
print("Factorial is:", fact(n))
