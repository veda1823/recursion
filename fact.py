def factorial(n):
    if n == 0:
        return 1
    smallAns = factorial(n - 1)
    ans = n * smallAns
    return ans

n = int(input())
print(factorial(n))
