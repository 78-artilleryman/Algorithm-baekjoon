def factorial(n):
    if n <= 1:
        ans = 1
    else:
        ans = factorial(n - 1) * n

    return ans

N = int(input())
print(factorial(N))