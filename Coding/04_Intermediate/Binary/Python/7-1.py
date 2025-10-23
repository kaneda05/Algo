import bisect
N, K = map(int,input().split())
A = list(map(int,input().split()))
x = list(map(int,input().split()))

for i in range(N):
    print(bisect.bisect_right(x,A[i]))
