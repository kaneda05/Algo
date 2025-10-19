from collections import deque

N, X = map(int, input().split())
P = list(map(int, input().split()))

sub = [[] for _ in range(N)]
for i in range(1, N):
    sub[P[i - 1]].append(i)

# --- BFS（キューを使う）---
q = deque([X])
cnt = 0

while q:
    v = q.popleft()
    for child in sub[v]:
        cnt += 1
        q.append(child)

print(cnt)
