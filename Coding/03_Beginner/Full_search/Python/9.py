N = int(input())
flag = True
if N >= 2:
    for i in range(2,N):
        if N%i==0:
            continue
        else:
            flag = False
else:
    flag = False

if flag:
    print("Yes")
else:
    print("No")