from collections import deque
import sys

N = int(input())
que = deque()

for i in range(N):
    order = list(map(int, sys.stdin.readline().strip().split()))
    if len(order) == 2:
        que.append(order[1]) if order[0] == 1 else que.appendleft(order[1])
    elif order[0] == 3:
        print(que.pop()) if que else print(-1)
    elif order[0] == 4:
       print(que.popleft()) if que else print(-1)
    elif order[0] == 5:
        print(len(que))
    elif order[0] == 6:
        print(1) if not que else print(0)
    elif order[0] == 7:
        print(que[-1]) if que else print(-1)
    elif order[0] == 8:
        print(que[0]) if que else print(-1)