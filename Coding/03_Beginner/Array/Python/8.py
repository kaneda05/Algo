H, W = map(int,input().split())
grid = [[0 for i in range(W)] for j in range(H)]

for i in range(H):
    S = input()
    for j in range(W):
        if S[j] == "#":
            grid[i][j] = 1

p, q = map(int,input().split())

ans = 0
for i in range(H):
    ans += grid[i][q]

for j in range(W):
    ans += grid[p][j]

ans -= grid[p][q]

print(ans)