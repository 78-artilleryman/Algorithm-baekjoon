from collections import deque

N = int(input())
case_number = deque(enumerate(map(int, input().split())))
result = []

while case_number:
    index, value = case_number.popleft()
    result.append(index + 1)

    if value > 0:
        case_number.rotate(-(value - 1))
    elif value < 0:
        case_number.rotate(-value)

print(' '.join(map(str, result)))


