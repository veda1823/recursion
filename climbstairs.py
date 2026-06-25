cur = []
ans = []

def f(pos, n):
    if pos > n:
        return

    if pos == n:
        ans.append(cur[:])
        return

    cur.append(1)
    f(pos + 1, n)
    cur.pop()

    cur.append(2)
    f(pos + 2, n)
    cur.pop()

n = int(input())
f(0, n)

for path in ans:
    print(*path)