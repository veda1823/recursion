import sys
sys.setrecursionlimit(10**7)

n = int(input())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

dp = [[-1] * n for _ in range(n)]

def f(i, j):

    # Last row
    if i == n - 1:
        return a[i][j]

    # Already calculated
    if dp[i][j] != -1:
        return dp[i][j]

    # Down
    ans1 = f(i + 1, j)

    # Down-Right
    ans2 = f(i + 1, j + 1)

    dp[i][j] = a[i][j] + min(ans1, ans2)

    return dp[i][j]

print(f(0, 0))