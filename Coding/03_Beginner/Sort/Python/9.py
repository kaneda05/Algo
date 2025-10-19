N, K = map(int,input().split())
L = []
for i in range(N):
    A, B = map(int,input().split())
    L.append((A,B))

L = sorted(L)
ans = 0
for a,b in L:
    if b <= K:
        K -= b
        ans += a * b
    elif K < b:
        ans += a * K
        break
    
print(ans)