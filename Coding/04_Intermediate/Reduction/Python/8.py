
N, D = map(int, input().split())
X = list(map(int, input().split()))

acc = [0] * (N+1)
for idx, x in enumerate(X):
    acc[idx+1] = acc[idx] + x

max_start, max_period_visitor = 0, 0
for idx in range(N-D+1):
    period_visitor = acc[idx+D] - acc[idx]
    if period_visitor >= max_period_visitor:
        max_start = idx
        max_period_visitor = period_visitor


max_end = max_start + D - 1

# 出力
print(f'{max_start}~{max_end}')