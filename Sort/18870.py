import sys
input =  sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

sort_nums = sorted(set(nums))

index_map = {value: idx for idx, value in enumerate(sort_nums)}
print(" ".join(str(index_map[x])for x in nums))