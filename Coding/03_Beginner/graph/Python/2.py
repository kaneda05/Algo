N, M = map(int,input().split())
follow = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int,input().split())
    follow[A].append(B)

for i in range(N):
    follow[i].sort()
    print(*follow[i])