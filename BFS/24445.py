from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, R = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

for _ in range(M):
    u, v = map(int,input().split())
    graph[v].append(u)
    graph[u].append(v)

for i in range(1, N+1):
    graph[i].sort(reverse=True)

def bfs(graph, start, visited):
    global cnt
    que = deque([start])
    visited[start] = cnt
    cnt += 1

    while que:
        v = que.popleft()
        for u in graph[v]:
            if not visited[u]:
                que.append(u)
                visited[u] = cnt
                cnt += 1
bfs(graph, R, visited)

for i in range(1, N+1):
    print(visited[i])