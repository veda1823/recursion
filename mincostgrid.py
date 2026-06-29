import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

INF = 10**18

dp = [[-1] * m for _ in range(n)]

def f(i, j):

    if i == n - 1 and j == m - 1:
        return a[i][j]

    if i >= n or j >= m:
        return INF

    if dp[i][j] != -1:
        return dp[i][j]

    # Right
    ans1 = f(i, j + 1)

    # Down
    ans2 = f(i + 1, j)

    dp[i][j] = a[i][j] + min(ans1, ans2)

    return dp[i][j]

print(f(0, 0))