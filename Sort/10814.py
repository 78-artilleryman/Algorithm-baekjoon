N = int(input())
result = []

for i in range(N):
    age, name = map(str, input().split())
    age = int(age)
    result.append([age, name])

result.sort(key = lambda x: x[0])

for i in range(N):
    print(str(result[i][0]) + " " + result[i][1])
