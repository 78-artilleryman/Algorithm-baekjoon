from collections import deque

N, K = map(int, input().split())
que = deque(i for i in range(1, N+1))
result = []

while que:
    que.rotate(-(K - 1))
    result.append(que.popleft())

result_str = "<" + ", ".join(map(str, result)) + ">"
print(result_str)

