N = int(input())
A = list(map(int,input().split()))
ans = 0
for i in range(1,N-1):
    if A[i-1] <= A[i] and A[i+1] <= A[i]:
        ans += 1
print(ans)