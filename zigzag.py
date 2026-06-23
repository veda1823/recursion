def zigzag(n):
    if n == 0:
        return

    print(n)

    zigzag(n - 1)

    if n != 1:
        print(n)

n = int(input())
zigzag(n)