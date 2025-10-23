N = int(input())

def f(x):
    return x*(x*(x+1)+2)+3

left = 0
right = 100
while right - left > 1e-4:
    mid = (left + right) / 2
    if (f(mid) < N):
        left = mid
    else:
        right = mid
    
print(left)