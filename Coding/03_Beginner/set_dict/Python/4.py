N = int(input())
S = list(input().split())
d = {}
for s in S:
    if s in d:
        d[s] += 1
    else:
        d[s] = 1


max_element = 0
ans = ""
for key, value in d.items():
    if max_element<value:
        ans = key
        max_element = value
    elif value == max_element and key < ans:
        ans = key

print(ans)