def sum(n):
    if n == 0:
        return 0
    smallAns = sum(n - 1)
    ans = n + smallAns
    return ans
n=int(input())
print(sum(n))
