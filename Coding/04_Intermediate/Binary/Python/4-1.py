import bisect
N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
for i in range(M):
    print(bisect.bisect_right(A,B[i]))