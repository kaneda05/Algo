H, W, x, y = map(int,input().split())
S = [input().strip() for _ in range(H)]
x -= 1
y -= 1
ans = []
for i in range(x,x+3):
    for j in range(y, y+3):
        ans.append(S[i][j])


for i in range(3):
    print("".join(ans[i*3:(i+1)*3]))
