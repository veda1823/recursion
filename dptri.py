import sys
sys.setrecursionlimit(10**7)

MOD = 10**9 + 7

n = int(input())

dp = [-1] * (n + 1)

def trib(x):
    if x == 0:
        return 0
    if x == 1 or x == 2:
        return 1

    if dp[x] != -1:
        return dp[x]

    dp[x] = (trib(x - 1) + trib(x - 2) + trib(x - 3)) % MOD
    return dp[x]

print(trib(n))