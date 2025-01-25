# 1차 코드 (시간 초과)
# N = int(input())
# case_number = []
# stack = []
#
# for _ in range(N):
#     line = input()  # 입력 받기
#     case_number.append(list(map(int, line.split())))
#
# for order in case_number:
#     if len(order) == 2:
#         stack.append(order[1])
#     elif order[0] == 2:
#         if stack:
#             print(stack.pop())
#         else:
#             print(-1)
#     elif order[0] == 3:
#         print(len(stack))
#     elif order[0] == 4:
#         if not stack:
#             print(1)
#         else:
#             print(0)
#     elif order[0] == 5:
#         if stack:
#             print(stack[-1])
#         else:
#             print(-1)

# 개선된 코드
import sys

N = int(input())
stack = []

for i in range(N):
    order = sys.stdin.readline().split()
    if len(order) == 2:
        stack.append(int(order[1]))
    elif order[0] == "2":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order[0] == "3":
        print(len(stack))
    elif order[0] == "4":
        if not stack:
            print(1)
        else:
            print(0)
    elif order[0] == "5":
        if stack:
            print(stack[-1])
        else:
            print(-1)