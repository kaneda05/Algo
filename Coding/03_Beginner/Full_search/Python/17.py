N = int(input())
A = list(map(int,input().split()))
cnt = 0
for i in range(N):
    if A[i] >= 2:
        flag = True
        for j in range(2,A[i]-1):
            if A[i] % j == 0:
                flag = False
        if flag:
            cnt += 1

print(cnt)