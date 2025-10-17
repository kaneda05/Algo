a, b = map(int,input().split())
a_divisor = []
b_divisor = []

if a == b:
    print("No")
    exit()

for i in range(1,a+1):
    if a % i == 0:
        a_divisor.append(i)

for i in range(1,b+1):
    if b % i == 0:
        b_divisor.append(i)


if sum(a_divisor)-a == b and sum(b_divisor)-b == a:
    print("Yes")
else:
    print("No")