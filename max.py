import sys
sys.setrecursionlimit(100000)

def findMax(A, N):
    if N == 1:
        return A[0]

    mx = findMax(A, N - 1)

    if A[N - 1] > mx:
        return A[N - 1]
    return mx

N = int(input())
A = list(map(int, input().split()))

print(findMax(A, N))