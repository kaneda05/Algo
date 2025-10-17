N = int(input())
cnt = 0
for i in range(N):
    S = input()
    if S == S[::-1]:
        cnt += 1
print(cnt)