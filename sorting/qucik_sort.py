from components.creat_list import creatingTheList
from typing import List, Generator, Tuple
import random

def randomized_quicksort(array: List[int], low: int, high: int) -> List[int]:
    if low < high:
        pivotIndex = randomize_pivot(array, low, high)
        randomized_quicksort(array, low, pivotIndex - 1)
        randomized_quicksort(array, pivotIndex + 1, high)
    return array

def randomize_pivot(array: List[int], low: int, high: int):
    randomIndex = random.randint(low, high)
    array[randomIndex], array[high] = array[high], array[randomIndex]
    return partion(array, low, high)

def partion(array: List[int], low: int, high: int):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def randomized_quick_sort_steps(array: List[int], low: int, high: int):
    if low < high:
        pivotIndex = yield from randomized_partition_steps(array, low, high)
        yield from randomized_quick_sort_steps(array, low, pivotIndex - 1)
        yield from randomized_quick_sort_steps(array, pivotIndex + 1, high)


def randomized_partition_steps(array: List[int], low: int, high: int) -> int:
    randIndex = random.randint(low, high)
    array[randIndex], array[high] = array[high], array[randIndex]  # random pivot
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        # yield current state: array copy, active index j, pivot index high
        yield (array.copy(), j, high)
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            # yield after swap
            yield (array.copy(), i, j)

    array[i + 1], array[high] = array[high], array[i + 1]
    # yield after final pivot placement
    yield (array.copy(), i + 1, high)
    return i + 1

if __name__ == '__main__':
    num: List[int] = creatingTheList(25)
    num2: List[int] = randomized_quicksort(num, 0, len(num) - 1)
    print(num2)