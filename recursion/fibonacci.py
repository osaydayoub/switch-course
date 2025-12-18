# Ex 1
# Fibonacci Sequence
# Problem: Write a recursive function that returns the nth number in the Fibonacci sequence.
# Example Input: fibonacci(6)
# Expected Output: 8

def fibonacci(n):
    if n==1 or n==0:
        return n
    return fibonacci(n-2)+fibonacci(n-1)

print(fibonacci(6))