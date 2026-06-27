import sys
sys.setrecursionlimit(200000)
def f(n):
    if n < 10:
        return n
    s = 0
    while n > 0:
        s += n % 10
        n //= 10

    return f(s)

n = int(input())
print(f(n))