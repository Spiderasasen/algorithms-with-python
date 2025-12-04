from components.creat_list import creatingTheList
from typing import List

def mergeSort(array: List[int]) -> List[int]:
    if len(array) <= 1:
        return array
    else:
        middle = len(array) // 2

        #recursion inside the mergesort function
        left = mergeSort(array[:middle])
        right = mergeSort(array[middle:])

        #calling the merge function
        sort: List[int] = merge(left, right)
        print(sort)
        return sort

def merge(left: List[int], right:List[int]) -> List[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
        print(result)
    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == '__main__':
    nums: List[int] = creatingTheList(10)
    nums2 = mergeSort(nums.copy())