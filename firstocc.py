import sys
sys.setrecursionlimit(200000)

def firstoc(arr, x, n):
    if n == 0:
        return -1

    smallAns = firstoc(arr, x, n - 1)

    if smallAns != -1:
        return smallAns

    return n if arr[n - 1] == x else -1

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

print(firstoc(arr, x, n))