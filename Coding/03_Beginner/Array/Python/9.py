H, W = map(int,input().split())
board = [input().strip() for _ in range(H)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

Q = int(input())
for i in range(Q):
    x, y = map(int,input().split())
    ans = 0
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < H and 0 <= ny < W:
            if board[nx][ny] == "#":
                ans += 1
    print(ans)