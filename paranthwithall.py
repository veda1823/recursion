s = list(input())
n = len(s)

ans = []

def f(i, open_cnt, close_cnt):
    if close_cnt > open_cnt:
        return

    if i == n:
        if open_cnt == close_cnt:
            ans.append("".join(s))
        return

    if s[i] == '?':
        s[i] = '('
        f(i + 1, open_cnt + 1, close_cnt)

        s[i] = ')'
        f(i + 1, open_cnt, close_cnt + 1)

        s[i] = '?'
    elif s[i] == '(':
        f(i + 1, open_cnt + 1, close_cnt)
    else:
        f(i + 1, open_cnt, close_cnt + 1)

f(0, 0, 0)

print(len(ans))
for x in ans:
    print(x)