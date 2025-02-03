N = int(input())
result = set()

for i in range(N):
    string = input()
    result.add(string)

sorted_result = sorted(result, key = lambda x : (len(x), x))

for string in sorted_result:
    print(string)