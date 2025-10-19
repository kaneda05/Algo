N = int(input())
A = [0] + list(map(int,input().split()))

cnt = {}
for i in range(N+1):
    for j in range(N+1):
        for k in range(N+1):
            score = A[i]+A[j]+A[k]
            cnt[score] = 1

print(len(cnt))