H, W = map(int,input().split())
S = [input().strip() for _ in range(H)]
T = [input().strip() for _ in range(H)]


cnt = 0
for i in range(H):
    for j in range(W):
        if S[i][j] != T[i][j]:
            cnt += 1
print(cnt)