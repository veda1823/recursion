import sys
sys.setrecursionlimit(100000)

def findMin(A, N):
    if N == 1:
        return A[0]

    mn = findMin(A, N - 1)

    if A[N - 1] < mn:
        return A[N - 1]
    return mn

N = int(input())
A = list(map(int, input().split()))

print(findMin(A, N))