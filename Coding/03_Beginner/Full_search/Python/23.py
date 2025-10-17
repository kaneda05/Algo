N = int(input())
S = [input() for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        if S[i] == S[j]:
            print("Yes")
            exit()

print("No")