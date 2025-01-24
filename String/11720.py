n = int(input())
number = input()
number_list = [int(digit) for digit in number]
result = 0

if(len(number_list) != n):
    print("입력값이 잘 못 됐습니다.")
else:
    for digit in number:
        result += int(digit)

print(result)

# n = int(input())
# number = input()
#
# if len(number) != n:
#     print("입력값이 잘못됐습니다.")
# else:
#     result = sum(int(digit) for digit in number)
#     print(result)