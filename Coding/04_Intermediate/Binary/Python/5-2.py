import bisect
N, K = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

for i in range(N):
    left = 0
    right = N
    while (left!=right):
        mid = (left+right) // 2
        if A[mid]>=K-A[i]:
            left = mid
        else:
            right = mid + 1
    ans += N - left
print(ans)