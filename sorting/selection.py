from components.creat_list import creatingTheList
from typing import List

#selection sort
def selection_sort(array: List[int]) -> List[int]:
    n = len(array)
    for i in range(0, n-1):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        # print(array)
    return array

#visulizer
def selection_sort_steps(array):
    n = len(array)
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            # highlight i (red) and j (green)
            yield array[:], i, j
            if array[j] < array[minIndex]:
                minIndex = j
                # highlight new minIndex (could use green again)
                yield array[:], i, minIndex
        # swap the found minimum into place
        array[i], array[minIndex] = array[minIndex], array[i]
        yield array[:], i, minIndex

if __name__ == '__main__':
    num = creatingTheList(10)
    num2 = selection_sort(num.copy())