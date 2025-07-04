s = input()
flag = True
cnt = 0
ans = 0
for i in range(len(s)-1):
    if flag:
        if s[i] == s[i+1]:
            cnt += 1
            ans = max(ans+1,cnt)
        else:
            cnt = 0
    else:
        flag = False

print(ans)
