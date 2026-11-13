from typing import List

def count_unique_words(words: List[str]) -> int:
    my_set = set(words)
    counter = 0
    for element in my_set:
        counter+=1
    return counter

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
