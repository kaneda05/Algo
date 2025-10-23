N, A, B = map(int,input().split())
grid = [[] for _ in range(N)]
for i in range(N):
    S = input()
    for j in range(N):
        if S[j] == "o":
            grid[i].append(j)

if B in grid[A]:
    print("Yes")
else:
    print("No")
