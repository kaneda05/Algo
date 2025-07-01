A, B = map(int,input().split())
for x in range(1,min(A,B)+1):
    if (A % x == 0 and  B % x == 0):
        ans = x

print(ans)