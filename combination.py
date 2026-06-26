cur=[]
ans=[]
def f(a,idx,sum):
    if sum==target:
        ans.append(cur[:])
        return
    if sum>target or idx>=n:
        return
    cur.append(a[idx])
    f(a,idx,sum+a[idx]);
    cur.pop()
    f(a,idx+1,sum)
n,target=map(int,input().split())
a=list(map(int,input().split()))    
f(a,0,0)
print(len(ans))
for x in ans:
    print(len(x), *x)   