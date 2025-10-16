N, V = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] == V:
        print("Yes")
        exit()

print("No")
