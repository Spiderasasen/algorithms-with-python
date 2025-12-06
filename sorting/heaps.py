from components.creat_list import creatingTheList
from typing import List

#max heap
def max_heap(array: List[int]) -> List[int]:
    n = len(array)

    #building a max heap
    for i in range(n// 2 - 1, -1, -1):
        max_heap_sort(array, n, i)

    for i in range(n -1 , -1, -1):
        array[0], array[i] = array[i], array[0]
        max_heap_sort(array, i, 0)

    return array

def max_heap_sort(array: List[int], n: int, i: int):
    largest: int = i
    left: int = 2*i + 1
    right: int = 2*i + 2

    #if the largest is at the left side of the heap
    if left < n and array[left] > array[largest]:
        largest = left
    #if the largest is at the right side of the heap
    if right < n and array[right] > array[largest]:
        largest = right
    #if the largest element is somewhere else in the heap
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heap_sort(array, n, largest)

#min heap
def min_heap(array: List[int]) -> List[int]:
    n = len(array)
    # building a max heap
    for i in range(n // 2 - 1, -1, -1):
        min_heap_sort(array, n, i)

    for i in range(n - 1, -1, -1):
        array[0], array[i] = array[i], array[0]
        min_heap_sort(array, i, 0)

    return array

def min_heap_sort(array: List[int], n: int, i: int):
    smallest = i
    left: int = 2*i + 1
    right: int = 2*i + 2

    #if the left element is the smallest
    if left < n and array[left] < array[smallest]:
        smallest = left
    #if the right element is tht smallest
    if right < n and array[right] < array[smallest]:
        smallest = right
    #if the smallest is somewhere in the heap
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heap_sort(array, n, smallest)


if __name__ == '__main__':
    #creating the list
    num: List[int] = creatingTheList(10)
    #max
    num2: List[int] = max_heap(num.copy())
    print(num2)
    #min
    num3: List[int] = min_heap(num.copy())
    print(num3)
    #min -> max
    num4: List[int] = min_heap(num2.copy())
    print(num4)
    #max -> min
    num5: List[int] = max_heap(num3.copy())
    print(num5)