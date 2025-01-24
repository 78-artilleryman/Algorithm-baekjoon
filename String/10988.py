# 큐를 이용한 1차 코드
#from collections import deque
#
# deque = deque()
# case_string = input()
#
# for char in case_string:
#     deque.append(char)
#
# def palindrome_check(que_array):
#
#     while len(que_array) > 1:
#         if que_array.popleft() != que_array.pop():
#             return 0
#         elif len(que_array) == 1:
#             que_array.pop()
#     return 1
#
# print(palindrome_check(deque))

# 개선
from collections import deque

def palindrome_check(string):
    string_deque = deque(string)

    while len(string_deque) > 1:
        if string_deque.popleft() != string_deque.pop():
            return 0
    return 1

case_string = input()
print(palindrome_check(case_string))

