def func(N, X):
    ans = N+1
    for i in range(5):
        ans = ans*X+1
    return ans

N, M = map(int,input().split())

left = 0
right = 100
while right - left > 1e-4:
    mid = (left + right) / 2
    if (func(N,mid)) < M:
        left = mid
    else:
        right = mid

print(left)