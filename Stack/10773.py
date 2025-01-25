# 1차 코드 (시간 3332 ms)
# def money_stack(array):
#     while len(array) > 0:
#         money = array.pop(0)
#
#         if money > 0:
#             stack.append(money)
#         else:
#             stack.pop()
#
#     return sum(stack)
#
# case_len = int(input())
# case_array = [int(input()) for _ in range(case_len)]
# stack = []
#
# print(money_stack(case_array))

# 개선된 코드 (시간 복잡도 개선, 시간 2576 ms)
# from collections import deque
#
# def money_stack(array):
#     que = deque(array)
#     while len(que) > 0:
#         money = que.popleft()
#
#         if money > 0:
#             stack.append(money)
#         else:
#             stack.pop()
#
#     return sum(stack)
#
# case_len = int(input())
# case_array = [int(input()) for _ in range(case_len)]
# stack = []
#
# print(money_stack(case_array))

# 2치 개선 (스택만 활용, 시간 2544 ms)
case_len = int(input())
stack = []

for _ in range(case_len):
    money = int(input())
    if money > 0:
        stack.append(money)
    else:
        stack.pop()

print(sum(stack))

