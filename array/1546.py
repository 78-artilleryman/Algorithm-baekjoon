result = []
sum1 = 0.0
x = float(input())

y = list(map(float, input().split()))

for i in range(len(y)):
    result.append(y[i]/max(y)*100)

    sum1 = sum1 + result[i]

print(sum1/x)