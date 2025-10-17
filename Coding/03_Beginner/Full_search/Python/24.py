N = int(input())
S = input()
l = []
N = len(S)
cnt = 0
for i in range(N):
    for j in range(i+1,N):
        if S[i] == S[j]:
            cnt += 1

print(cnt)