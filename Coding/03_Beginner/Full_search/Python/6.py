N = int(input())
A = list(map(int,input().split()))
ans = 10**5
for a in A:
    if ans > a:
        ans = a
print(ans)