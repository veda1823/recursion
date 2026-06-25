import sys
sys.setrecursionlimit(100000)
cur=[]
ans=[]
def f(a,idx):
    if idx== n:
        ans.append(cur[:])
        return
    cur.append(a[idx])
    f(a,idx+1)  
    cur.pop()
    f(a,idx+1)
n=int(input())
a=list(map(int,input().split()))
f(a,0)
for i in ans:
    print(*i)  