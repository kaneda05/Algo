N = int(input())
A = list(map(int,input().split()))

max_A = max(A)
ans = 0
for i in range(N):
    if A[i] == max_A:
        ans += 1
print(ans)