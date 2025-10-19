N = int(input())
A = list(map(int,input().split()))
n = len(set(A))
ans = len(A) - n
print(ans)