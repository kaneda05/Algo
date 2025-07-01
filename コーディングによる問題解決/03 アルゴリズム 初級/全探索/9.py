N = int(input())

if N >= 2:
    flag = True
    for i in range(2,N//2):
        if N % i == 0:
            flag = False
else:
    flag = False

print("Yes" if flag else "No")