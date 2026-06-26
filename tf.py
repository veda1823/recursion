n = int(input())

maze = []
for _ in range(n):
    maze.append(list(map(int, input().split())))

visited = [[False] * n for _ in range(n)]
cur = []
ans = []

def f(i, j):
    if i < 0 or i >= n or j < 0 or j >= n or visited[i][j] or maze[i][j] == 0:
        return

    if i == n - 1 and j == n - 1:
        ans.append("".join(cur))
        return

    visited[i][j] = True

    # Down
    cur.append('D')
    f(i + 1, j)
    cur.pop()

    # Left
    cur.append('L')
    f(i, j - 1)
    cur.pop()

    # Right
    cur.append('R')
    f(i, j + 1)
    cur.pop()

    # Up
    cur.append('U')
    f(i - 1, j)
    cur.pop()

    visited[i][j] = False


if maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
    print(0)
else:
    f(0, 0)
    ans.sort()

    if len(ans) == 0:
        print(0)
    else:
        print(len(ans))
        for path in ans:
            print(path)