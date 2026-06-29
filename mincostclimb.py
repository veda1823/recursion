import sys
sys.setrecursionlimit(10**7)
n = int(input())
a = [0] + list(map(int, input().split()))
dp = [-1] * (n + 2)
def f(pos):
    if pos > n:
        return 0
    if pos == n:
        return a[n]
    if dp[pos] != -1:
        return dp[pos]
    ans1 = f(pos + 1)
    ans2 = f(pos + 2)
    dp[pos] = a[pos] + min(ans1, ans2)
    return dp[pos]
print(min(f(1), f(2)))