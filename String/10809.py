case_string = input()
result_dict = {chr(i): -1 for i in range(97, 123)}

for i, value in enumerate(case_string):
    if result_dict[value] == -1:
        result_dict[value] = i

print(" ".join(map(str, result_dict.values())))