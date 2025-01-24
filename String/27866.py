first_input = input("")
second_input = input()

def string_index_return(first_input: str, second_input: int) -> str:
    index = second_input - 1
    return first_input[index]

print(string_index_return(first_input, int(second_input)))