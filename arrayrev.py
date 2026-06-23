def printArray(A, N):
    if N == 0:
        return
    print(A[N - 1], end=" ")
    printArray(A, N - 1)


N = int(input())
A = list(map(int, input().split()))

printArray(A, N)