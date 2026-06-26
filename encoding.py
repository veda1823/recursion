cur=[]
ans=[]
def getAlphabet(num):
    return chr(ord('a')+num-1)
def f(s,idx):
    if idx==len(s):
        ans.append("".join(cur))
        return
    num=int(s[idx])
    if num>=1 and num<=9:
        cur.append(getAlphabet(num))
        f(s,idx+1)
        cur.pop()
        if idx+1<len(s):
            num2=int(s[idx:idx+2])
            if num2>=10 and num2<=26:
                cur.append(getAlphabet(num2))
                f(s,idx+2)
                cur.pop()
s=input().strip()
f(s,0)
print(len(ans))
for x in ans:
    print(x)