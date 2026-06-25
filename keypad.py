s = input()

choices = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

cur = []
ans = []

def f(idx):
    if idx == len(s):
        ans.append("".join(cur))
        return

    digit = int(s[idx])

    for ch in choices[digit]:
        cur.append(ch)
        f(idx + 1)
        cur.pop()

f(0)

print(len(ans))
for x in ans:
    print(x)