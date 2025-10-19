N = int(input())
A = list(map(int,input().split()))

for i in range(1, N):
    while i and A[i-1] > A[i]:
        A[i-1], A[i] = A[i], A[i-1]
        i -= 1
    print(*A)