S = input()
c = input()
flag = False
for s in S:
    if c == s:
        flag = True
print("Yes" if flag else "No")