import sys
sys.setrecursionlimit(10**6)
def power(x, n):
    if n == 0:
        return 1
    smallAns = power(x, n - 1)
    if n % 2 == 0:
        return smallAns * smallAns
    else:
        return x * smallAns * smallAns
x,n = map(int, input().split())
print(power(x,n));