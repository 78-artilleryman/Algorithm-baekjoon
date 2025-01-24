# defaultdict를 이용한 코드 (시간 152ms)
# from collections import defaultdict
#
# def max_char(string):
#     # 빈도수를 저장할 defaultdict
#     char_count = defaultdict(int)
#     upper_change_string = string.upper()
#
#     # 빈도수 계산
#     for char in upper_change_string:
#         char_count[char] += 1
#
#     # 최대 빈도 계산
#     max_count = max(char_count.values())
#     max_chars = [char for char, count in char_count.items() if count == max_count]
#
#     # 최대 빈도를 가진 문자가 2개 이상인 경우 '?' 반환
#     if len(max_chars) > 1:
#         return '?'
#
#     # 최대 빈도를 가진 문자가 하나인 경우 반환
#     return max_chars[0]
#
# case_string = input()
# print(max_char(case_string))

# Counter를 이용한 코드 (시간 116ms)
from collections import Counter

def max_char(string):
    char_count = Counter(string.upper())

    max_count = max(char_count.values())
    max_chars = [char for char, count in char_count.items() if count == max_count]

    if len(max_chars) > 1:
        return '?'

    return max_chars[0]

case_string = input()
print(max_char(case_string))