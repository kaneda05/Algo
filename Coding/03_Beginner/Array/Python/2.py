Q = int(input())
Array = [3,1,4,1,5,9,2,6,5,3]

for i in range(Q):
    query = list(map(int,input().split()))
    k = query[1]
    if query[0] == 0:
        print(Array[k])
    else:
        v = query[2]
        Array[k] = v