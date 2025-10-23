import bisect
N = int(input())
W = list(map(int,input().split()))
A = W.copy()
A.sort()
for i in range(N):
    print(bisect.bisect_left(A,W[i]))
