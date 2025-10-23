from collections import defaultdict

N, M, X = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

friends = set(graph[X])

fof = set()

for f in friends:
    for ff in graph[f]:
        if ff != X and ff not in friends:
            fof.add(ff)

print(len(fof))
