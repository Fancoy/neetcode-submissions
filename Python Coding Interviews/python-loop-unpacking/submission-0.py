from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    best_name = scores[0][0]
    best_score = scores[0][1]
    for element in scores:
        x, y = element[0], element[1]
        if y > best_score:
            best_name = element[0]
            best_score = element[1]
    return best_name


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
