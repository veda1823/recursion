import sys
sys.setrecursionlimit(10**7)
MOD = 10**9 + 7
n = int(input())
dp = [-1] * (n + 1)
def fib(x):
    if x == 0:
        return 0
    if x == 1:
        return 1

    if dp[x] != -1:
        return dp[x]

    dp[x] = (fib(x - 1) + fib(x - 2)) % MOD
    return dp[x]

print(fib(n))