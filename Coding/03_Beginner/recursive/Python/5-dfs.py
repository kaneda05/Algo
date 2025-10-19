N, X = map(int, input().split())
P = list(map(int, input().split()))


sub = [[] for _ in range(N)]
for i in range(1, N):
    sub[P[i - 1]].append(i)


stack = [X]
cnt = 0

while stack:
    v = stack.pop()
    for child in sub[v]:
        cnt += 1
        stack.append(child)

print(cnt)
