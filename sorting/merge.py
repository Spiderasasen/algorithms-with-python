from components.creat_list import creatingTheList
from typing import List

#merge sort function
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
        # print(sort)
        return sort

#merge function (could call again)
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
        # print(result)
    result.extend(left[i:])
    result.extend(right[j:])
    return result

#merge sort steps visualizer
def merge_sort_steps(array: List[int]):
    yield array[:], None, None
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left = array[:mid]
    right = array[mid:]

    left_sorted: List[int] = yield from merge_sort_steps(left)   # get final sorted left
    right_sorted: List[int] = yield from merge_sort_steps(right) # get final sorted right

    merged:List[int] = []
    i = j = 0
    while i < len(left_sorted) and j < len(right_sorted):
        #makes a sythitic state of visual
        state = merged + left_sorted[i:] + right_sorted[j:]

        #computes highlight indices within state
        active_index = len(merged) #for left candiaite
        compare_index = len(merged) + (len(left_sorted) - i) #for right caniadate

        # highlight comparison
        yield state, active_index, compare_index

        if left_sorted[i] <= right_sorted[j]:
            merged.append(left_sorted[i])
            i += 1
        else:
            merged.append(right_sorted[j])
            j += 1
        yield merged + left_sorted[i:] + right_sorted[j:], i, j

        #post-append frame
        state = merged + left_sorted[i:] + right_sorted[j:]

        #recomputing the indeices
        active_index = len(merged)  # for left candiaite
        compare_index = len(merged) + (len(left_sorted) - i)  # for right caniadate

        yield state, active_index, compare_index

    #append finals
    merged.extend(left_sorted[i:])
    merged.extend(right_sorted[j:])

    #drawing the final vision
    yield merged, None, None
    return merged

if __name__ == '__main__':
    nums: List[int] = creatingTheList(10)
    nums2 = mergeSort(nums.copy())