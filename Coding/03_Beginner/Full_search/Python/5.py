N = int(input())
A = list(map(int,input().split()))
ans = -1
for i in range(N):
    if ans < A[i]:
        ans = A[i]
print(ans)