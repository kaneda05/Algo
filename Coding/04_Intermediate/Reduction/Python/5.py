N = int(input())
A = list(map(int, input().split()))

total = sum(A)
squares = sum(x * x for x in A)

ans = (total * total - squares) // 2
print(ans)
