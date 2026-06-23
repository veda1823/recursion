import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n==1:
        return 0
    if n==2:
        return 1
    smallAns1=f(n-1)
    smallAns2=f(n-2)
    ans=smallAns1+smallAns2
    return ans 
n=int(input())
print(f(n)) 