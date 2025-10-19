N = int(input())
A = list(map(int, input().split()))
A.sort()
if N % 2 == 0:
    print((A[(N//2)-1]+A[(N//2)])/2)
else:
    print(A[(N//2)])