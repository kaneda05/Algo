N, V = map(int,input().split())
A = list(map(int,input().split()))
vlist = [-1]
for i in range(N):
    if V == A[i]:
        vlist.append(i)
        
print(max(vlist))