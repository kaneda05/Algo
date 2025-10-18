L, R = map(int, input().split())

# 一の位ごとの出現回数（0〜9）
count = [0] * 10

for i in range(L, R + 1):
    last_digit = i % 10
    count[last_digit] += 1

ans = 0
for c in count:
    ans += c * (c - 1) // 2

print(ans)