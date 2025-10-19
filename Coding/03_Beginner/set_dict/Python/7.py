N = int(input())
A = list(map(int, input().split()))

d = {}
for a in A:
    d[a] = d.get(a, 0) + 1

ans = 0
for v, c in d.items():
    if c >= v:
        ans += c - v
    else:
        ans += c

print(ans)
