A, B = map(int,input().split())
N = min(A, B)
for i in range(1,N+1):
    if A % i == 0 and B % i == 0:
        ans = i
print(ans)