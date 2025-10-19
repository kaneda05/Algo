import sys
sys.setrecursionlimit(10**7)
A, B = map(int,input().split())

def f(x):
    if x == 0:
        return 0
    return f(x-1) + x

print(f(B)-f(A))