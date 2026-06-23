import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n==0:
        return 0
    smallAns=f(n//10)
    ans=smallAns+(n%10)
    return ans
n=int(input())
print(f(n))