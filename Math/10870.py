def fibonacci_numbers(n):
    if n <= 1:
        return n
    return fibonacci_numbers(n - 1) + fibonacci_numbers(n - 2)

N = int(input())
print(fibonacci_numbers(N))