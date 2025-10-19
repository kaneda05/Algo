import sys
sys.setrecursionlimit(10**7)

def f(x):
    if x == 0:
        return 0
    return f(x-1) + x

N = int(input())
print(f(N))
