import random
from typing import List


def insertionSort(array: List[int]) -> List[int]:
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
        print(array)
    return array

def creatingTheList(n: int) -> List[int]:
    numbers = []
    for i in range(n):
        num: int = random.randint(1, n)
        if num not in numbers:
            numbers.append(num)
    print(numbers)
    return numbers

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