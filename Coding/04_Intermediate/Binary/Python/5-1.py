import bisect
N, K = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
ans = 0
for i in range(N):
    ans += N - bisect.bisect_right(A,K-A[i])
print(ans)