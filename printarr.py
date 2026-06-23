def printArray(A, N):
    if N == 0:
        return
    printArray(A, N - 1)
    print(A[N - 1], end=" ")


N = int(input())
A = list(map(int, input().split()))

printArray(A, N)