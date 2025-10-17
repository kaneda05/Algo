S = input()
cnt = 0
for i in range(len(S)):
    flag = True
    for j in range(i+1,len(S)):
        if S[i] == S[j]:
            flag = False
    if flag:
        cnt += 1

print(cnt)