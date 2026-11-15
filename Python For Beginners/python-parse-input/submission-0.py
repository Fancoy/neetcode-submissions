from typing import List

def read_integers() -> List[int]:
    int_input = input()
    int_split = int_input.split(",")
    int_list = []
    for x in int_split:
        int_list.append(int(x))
    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
