N = int(input())
A = list(map(int,input().split()))
ans = 0
maxA = A[0]
for i in range(1,N):
    if maxA < A[i]:
        maxA = A[i]
        ans = i
print(ans)