k = int(input())

cur = []

def f(s):
    if s == k:
        print(*cur)
        return

    for i in range(1, 7):
        if s + i <= k:
            cur.append(i)
            f(s + i)
            cur.pop()

f(0)