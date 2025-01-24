dict = {
    1: [],
    2: ["A","B","C"],
    3: ["D","E","F"],
    4: ["G","H","I"],
    5: ["J","K","L"],
    6: ["M","N","O"],
    7: ["P","Q","R","S"],
    8: ["T","U","V"],
    9: ["W","X","Y","Z"],
}

test_string = input()
number_array = []


for char in test_string:
    for number in dict.items():
        if char in number[1]:
            number_array.append(number[0])

result = sum([x + 1 for x in number_array])
print(result)