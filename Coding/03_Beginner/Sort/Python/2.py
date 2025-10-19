N = int(input())
A = list(map(int,input().split()))

for i in range(N-1):
    min_index = A[i:].index(min(A[i:])) + i
    A[i], A[min_index] = A[min_index], A[i]
    print(*A)