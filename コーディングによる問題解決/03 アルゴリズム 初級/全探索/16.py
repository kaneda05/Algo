N, M, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

cnt = 0
for i in range(N):
    for j in range(M):
        if A[i] + B[j] == K:
            cnt += 1
print(cnt)