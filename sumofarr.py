def sum(arr,n):
    if n == 0:
        return 0
    return sum(arr,n-1)+arr[n-1]
n=int(input())
arr=list(map(int,input().split()))  
print(sum(arr,n))