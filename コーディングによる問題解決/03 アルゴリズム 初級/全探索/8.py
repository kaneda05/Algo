N = int(input())
A = list(map(int,input().split()))
cnt = 0
for i in range(1,N):
    if A[i-1] < A[i]:
        cnt += 1
print(cnt)