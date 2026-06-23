import sys
sys.setrecursionlimit(200000)

ans = []

def findAllOcc(A, N, X):
    if N == 0:
        return

    findAllOcc(A, N - 1, X)

    if A[N - 1] == X:
        ans.append(N)   # 1-based index

N = int(input())
A = list(map(int, input().split()))
X = int(input())

findAllOcc(A, N, X)

if len(ans) == 0:
    print(-1)
else:
    print(*ans)