def recursion(string, start, end, sum):
    if start >= end: return [1, sum + 1]
    elif string[start] != string[end]: return [0, sum + 1]
    else: return recursion(string, start + 1, end - 1, sum + 1)


def isPalindrome(string):
    sum = 0
    return recursion(string, 0, len(string)-1, sum)

N = int(input())

for i in range(N):
    string = input()
    print(*isPalindrome(string))


