# 1차 코드 (실패함)
# from collections import deque
#
# case_len = int(input())
# case_number = list(map(int, input().split()))
# que = deque(case_number)
# rating_stack = []
#
# min_number = min(case_number)
#
# while len(que) != 0:
#
#     if que[0] > min_number:
#         if  rating_stack and rating_stack[-1] - que[0] != 1:
#             print("Sad")
#             break
#         else:
#             print("top",que[0])
#             rating_stack.append(que.popleft())
#
#     elif que[0] == min_number:
#         print("bottom" , que[0])
#         que.popleft()
#         min_number += 1
#
# if not que:
#     print("Nice")

# 개선된 코드
N = int(input())
students = list(map(int, input().split()))
stack = []
min_number = 1

for student in students:
    stack.append(student)

    while stack and stack[-1] == min_number:
        stack.pop()
        min_number += 1

if stack:
    print("Sad")
else:
    print("Nice")