from typing import List
from components.creat_list import creatingTheList

#sorting
def bubbleSort(array: List[int]) -> List[int]:
    n = len(array)
    while True:
        swapped: bool = False
        for j in range(0, n-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
                # print(array)
        n = n - 1
        if not swapped:
            break
    return array

#visulizer
def bubble_sort_steps(array):
    n = len(array)
    swapped: bool = True
    while swapped:
        swapped = False
        for j in range (0, n-1):
            #yielding before comparison
            yield array[:], j, j+1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
                #yield after swap
                yield array[:], j, j+1
        n -= 1

def main():
    num = creatingTheList(10)
    print(num)
    num2 = bubbleSort(num.copy())
    print(num2)


if __name__ == '__main__':
    main()