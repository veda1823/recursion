import sys 
sys.setrecursionlimit(10**6)
def hanoi(n, a, b, c):
    if n == 1:
        print("Move", a, "to", c)
        return
 
    hanoi(n-1, a, c, b)
    print("Move", a, "to", c)
    hanoi(n-1, b, a, c)
 
n = int(input())
hanoi(n, "A", "B", "C")