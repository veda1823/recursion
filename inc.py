def printinc(n):
    if n==0:
        return
    printinc(n-1)
    print(n)
n=int(input())
printinc(n)