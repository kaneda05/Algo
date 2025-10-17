N = int(input())
A = list(map(int,input().split()))
ans = 0
for i in range(N):
    for j in range(i):
        for k in range(j):
            if A[i] <= A[j] and A[k] <= A[j]:
                ans += 1

print(ans)