# dfs를 사용한 풀이과정

# import sys
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline
#
# N = int(input())
# M = int(input())
# graph = [[] for _ in range(N + 1)]
# visited = [0] * (N + 1)
#
# for i in range(M):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)
#
# def dfs(graph, start, visited):
#     visited[start] = 1
#
#     for vv in graph[start]:
#         if not visited[vv]:
#             dfs(graph, vv, visited)
#
# dfs(graph, 1, visited)
# print(sum(visited) - 1)


# bfs를 사용한 풀이과정
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph,start, visited):
    que = deque([start])
    visited[start] = 1

    while que:
        vv = que.popleft()

        for n in graph[vv]:
            if visited[n] == 0:
                que.append(n)
                visited[n] = 1

bfs(graph, 1, visited)
print(sum(visited) - 1)