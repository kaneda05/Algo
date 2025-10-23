N, M = map(int,input().split())
cnt = 0
for x in range(1,N+1):
    for y in range(1,N+1):
        max_z = min(N, M-x-y)
        if max_z <= 0:
            continue
        cnt += max_z
    
print(cnt)