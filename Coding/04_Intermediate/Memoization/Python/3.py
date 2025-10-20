N, M = map(int,input().split())
cnt = 0
for x in range(1,N+1):
    for y in range(1,N+1):
        if M >= x + y:
            cnt += 1
    
print(cnt)