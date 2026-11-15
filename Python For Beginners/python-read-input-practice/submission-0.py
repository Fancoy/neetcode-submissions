def add_two_numbers() -> int:
    inputy = input()
    input_split = inputy.split(",")
    temp_list = []
    for element in input_split:
        temp_list.append(int(element))
    return temp_list[0] + temp_list[1]


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
