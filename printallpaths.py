cur=[]
ans=[]
def f(i,j):
    if i>=n or j>=m or a[i][j]==1:
        return
    if i==n-1 and j==m-1:
        ans.append(cur[:])
        return
    cur.append('R')
    f(i,j+1)
    cur.pop()
    cur.append('D')
    f(i+1,j)
    cur.pop()
n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
f(0,0 )
for path in ans:
    print(''.join(path))