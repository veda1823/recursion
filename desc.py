def printdesc(n):
    if n==0:
        return
    print(n)
    printdesc(n-1)
n=int(input())
printdesc(n)