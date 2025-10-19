N, M = map(int,input().split())
A = list(map(int,input().split()))
X = list(map(int,input().split()))
A.sort()
for i in range(M):
    print(A[X[i]])