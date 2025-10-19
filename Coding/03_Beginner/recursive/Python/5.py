import sys
sys.setrecursionlimit(10**7)

N, X = map(int,input().split())
P = list(map(int,input().split()))

def count_sub(x):
    total = 0
    for child in sub[x]:
        total += 1
        total += count_sub(child)
    return total

sub = [[] for _ in range(N)]
for i in range(1, N):
    sub[P[i-1]].append(i)

print(count_sub(X))