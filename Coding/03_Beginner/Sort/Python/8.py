N, K = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
ans = float("inf")
for i in range(N-K+1):
    diff = A[i+k-1]-A[i]
    ans = min(ans, diff)

print(ans)