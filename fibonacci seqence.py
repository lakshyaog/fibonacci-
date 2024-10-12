def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b  # Update values
    return sequence

# Get user input
try:
    count = int(input("Enter the number of Fibonacci numbers to generate: "))
    if count < 0:
        print("Please enter a non-negative integer.")
    else:
        fib_sequence = fibonacci(count)
        print("Fibonacci sequence:", fib_sequence)
except ValueError:
    print("Invalid input. Please enter an integer.")
