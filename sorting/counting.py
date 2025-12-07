from components.creat_list import creatingTheList
from typing import List, Generator, Tuple

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

def counting_sort_steps(array: List[int]) -> Generator[Tuple[List[int], int, List[int]], None, None]:
    k = max(array) + 1
    count = [0] * k

    for idx, element in enumerate(array):
        count[element] += 1
        yield (array.copy(), idx, count.copy())

    for i in range(1, k):
        count[i] += count[i - 1]
        yield (array.copy(), i, count.copy())

    output = [0] * len(array)
    for idx, element in enumerate(reversed(array)):
        pos = count[element] - 1
        output[pos] = element
        count[element] -= 1
        yield (output.copy(), pos, count.copy())

    yield (output.copy(), -1, count.copy())

if __name__ == '__main__':
    num: List[int] = creatingTheList(10)
    num2: List[int] = counting_sort(num.copy())
    print(num2)