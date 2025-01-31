import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(i, j):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]

        if (0 <= ni < N) and (0 <= nj < M):
            if graph[ni][nj] == 1:
                graph[ni][nj] = -1
                dfs(ni, nj)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                dfs(i, j)
                cnt += 1

    print(cnt)