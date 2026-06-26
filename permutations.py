n = int(input())
a = list(map(int, input().split()))
cur = [None] * n
ans = []
def f(idx):
    if idx == n:
        ans.append(cur[:])
        return

    for i in range(n):
        if cur[i] is None:
            cur[i] = a[idx]
            f(idx + 1)
            cur[i] = None

f(0)

print(len(ans))
for x in ans:
    print(*x)