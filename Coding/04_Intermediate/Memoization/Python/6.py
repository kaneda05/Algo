N = int(input())
A = list(map(int,input().split()))

acc = [0] * (N+1)
for i in range(N):
    acc[i+1] = acc[i] + A[i]

Q = int(input())
for _ in range(Q):
    k = int(input())
    print(acc[k])