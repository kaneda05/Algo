H, W = map(int,input().split())
grid = [input().strip() for _ in range(H)]


cnt = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == "o":
            cnt += 1
print(cnt)