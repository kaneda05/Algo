import bisect
N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

for i in range(M):
    left = 0
    right = N 
    while (lect != right):
        mid = (left + right) // 2
        if (A[mid] > B[i]):
            left = mid
        else:
            right = mid+1

    print(left)