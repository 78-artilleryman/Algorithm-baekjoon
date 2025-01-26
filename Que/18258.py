from collections import deque
import sys

N = int(input())
que = deque()

for i in range(N):
    order = sys.stdin.readline().split()

    if len(order) == 2:
        que.append(order[1])
    elif order[0] == "pop":
        if not que:
            print("-1")
        else:
            print(que.popleft())
    elif order[0] == "size":
        print(len(que))
    elif order[0] == "empty":
        if not que:
            print("1")
        else:
            print("0")
    elif order[0] == "front":
        if not que:
            print("-1")
        else:
            print(que[0])
    elif order[0] == "back":
        if not que:
            print("-1")
        else:
            print(que[-1])
