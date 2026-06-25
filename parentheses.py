def f(open, close):
    if close == n:
        ans.append(''.join(cur))
        return

    if open < n:
        cur.append('(')
        f(open + 1, close)
        cur.pop()

    if close < open:
        cur.append(')')
        f(open, close + 1)
        cur.pop()

n = int(input())

cur = []
ans = []

f(0, 0)

print(len(ans))
for s in ans:
    print(s)