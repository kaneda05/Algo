N, M = map(int,input().split())
menu = {}
for i in range(N):
    F, C = input().split()
    menu[F] = int(C)

X = list(input().split())
ans = 0
for x in X:
    ans += menu[x]

print(ans)
