import sys
sys.setrecursionlimit(10**7)

def func(x):
    if x == 1: return 1
    if x == 2: return 2
    return x * func(x-2)

N = int(input())
print(func(N))