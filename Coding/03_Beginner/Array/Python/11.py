H, W, sx, sy = map(int,input().split())
board = [input().strip() for _ in range(H)]

N = int(input())
T = input()

for i in range(N):
    if T[i] == "U":
        if 0 <= sx-1 < H and 0 <= sy < W and board[sx-1][sy] != "#":
            sx -= 1
    
    if T[i] == "D":
        if 0 <= sx+1 < H and 0 <= sy < W and board[sx+1][sy] != "#":
            sx += 1

    if T[i] == "L":
        if 0 <= sx < H and 0 <= sy-1 < W and board[sx][sy-1] != "#":
            sy -= 1

    if T[i] == "R":
        if 0 <= sx < H and 0 <= sy+1 < W and board[sx][sy+1] != "#":
            sy += 1

print(sx,sy)