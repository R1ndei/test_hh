# Task 1

def task(array: str) -> str:
    for i in range(len(array)):
        if not int(array[i]) or not int(array[i + 1]):
            return f"OUT: {i}"
    return "0 is not in list"


print(task("111111111110000000000000000"))


# Task 2
def task2(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int) -> str:
    min_1x = min(x1, x2)
    max_1x = max(x1, x2)
    min_1y = min(y1, y2)
    max_1y = max(y1, y2)

    min_2x = min(x3, x4)
    max_2x = max(x3, x4)
    min_2y = min(y3, y4)
    max_2y = max(y3, y4)

    x_1 = max(min_1x, min_2x)
    x_2 = min(max_1x, max_2x)
    y_1 = max(min_1y, min_2y)
    y_2 = min(max_1y, max_2y)

    if x_2 - x_1 < 0 or y_2 - y_1 < 0:
        return f"OUT: {False}"

    else:
        area = abs(y_2 - y_1) * abs(x_2 - x_1)
        return '{:.2f}'.format(area)


print(task2(1, 1, 3, 3, 2, 2, 4, 4))
