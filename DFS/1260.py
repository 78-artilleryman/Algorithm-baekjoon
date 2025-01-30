from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, R = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited_d = [0] * (N+1)
visited_b = [0] * (N+1)

for _ in range(M):
    u, v = map(int,input().split())
    graph[v].append(u)
    graph[u].append(v)

for i in range(1, N+1):
    graph[i].sort()

def dfs(graph, start, visited):
    visited[start] = 1
    print(start, end=' ')

    for vv in graph[start]:
        if not visited[vv]:
            dfs(graph, vv, visited)

def bfs(graph, start, visited):
    que = deque([start])
    visited[start] = 1

    while que:
        vv = que.popleft()
        print(vv, end=" ")
        for v in graph[vv]:
            if not visited[v]:
                que.append(v)
                visited[v] = 1

dfs(graph, R, visited_d)
print()
bfs(graph, R, visited_b)




