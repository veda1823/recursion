n = int(input())

board = [['.' for _ in range(n)] for _ in range(n)]
results = []

def canplace(row, col):
    # Same column
    i = row
    while i >= 0:
        if board[i][col] == 'Q':
            return False
        i -= 1

    # Upper-left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Upper-right diagonal
    i = row
    j = col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def find(row):
    if row == n:
        ans = []
        for r in board:
            ans.append("".join(r))
        results.append(ans)
        return

    for col in range(n):
        if canplace(row, col):
            board[row][col] = 'Q'
            find(row + 1)
            board[row][col] = '.'


find(0)

print(len(results))
for k in range(len(results)):
    for row in results[k]:
        print(row)
    if k != len(results) - 1:
        print()