N = int(input())
A = list(map(int,input().split()))

for i in range(N):
    minA = A[i]
    for i in range(i+1,N-1):
        if minA > A[i]:
            minA = A[i]
            index = i
    A[i],A[index] = A[index], A[i]
    print(*A)