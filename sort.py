def sort(arr, n):
    if n==1:
        return True
    return sort(arr, n-1) and arr[n-2] <= arr[n-1]
n=int(input())
arr=list(map(int,input().split()))
print(sort(arr,n))