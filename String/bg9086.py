test_len = int(input())
case_array = [input() for _ in range(test_len)]
result_array = [f"{char[0]}{char[-1]}" for char in case_array]
print('\n'.join(result_array))
