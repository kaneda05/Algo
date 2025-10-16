N, V = map(int,input().split())
A = list(map(int,input().split()))

flag = False
for i in range(N):
    if A[i] == V:
        ans = i
        flag = True

if flag:
    print(ans)
else:
    print(-1)