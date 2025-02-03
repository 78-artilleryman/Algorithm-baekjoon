N = int(input())
result = []

for i in range(N):
    x, y = map(int, input().split())
    result.append([x, y])

result.sort(key = lambda x : (x[1], x[0]))


for i in range(N):
    print(result[i][0], result[i][1])