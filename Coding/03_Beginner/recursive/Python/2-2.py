import sys
sys.setrecursionlimit(10**7)
A, B = map(int,input().split())

def func(A, N):
    if N < A:
        return 0
    return N + func(A, N-1)

print(func(A,B))