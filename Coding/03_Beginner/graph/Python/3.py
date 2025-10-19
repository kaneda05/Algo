N, M = map(int,input().split())
frends = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int,input().split())
    frends[A].append(B)
    frends[B].append(A)

max_frends = 0
for i in range(N):
    if max_frends < len(frends[i]):
        max_frends = len(frends[i])

for i in range(N):
    if max_frends == len(frends[i]):
        frends[i].sort()
        print(*frends[i])
        exit()