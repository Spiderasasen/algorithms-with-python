import random
from typing import List

#sorting
def insertionSort(array: List[int]) -> List[int]:
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
        # print(array)
    return array

#visulizer
def insertion_sort_steps(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        # highlight the key
        yield array[:], i, j
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
            yield array[:], i, j  # yield after each shift
        array[j + 1] = key
        yield array[:], i, None  # yield after placing key

def main():
    numbers = []
    for i in range(10):
        numbers.append(random.randint(1, 100))

    print(numbers)
    numbers2 = numbers.copy()
    insertionSort(numbers2)
    print(numbers2)

if __name__ == '__main__':
    main()