from components.creat_list import creatingTheList
from typing import List

#counting sort, console
def counting_sort(array: List[int]) -> List[int]:
    k = max(array) + 1
    count = [0] * k

    #counts occourances
    for element in array:
        count[element] += 1

    #cumlative counts
    for i in range(1, k):
        count[i] += count[i - 1]

    #build the output
    output = [0] * len(array)
    for element in array:
        output[count[element] - 1] = element
        count[element] -= 1

    return output

if __name__ == '__main__':
    num: List[int] = creatingTheList(10)
    num2: List[int] = counting_sort(num.copy())
    print(num2)