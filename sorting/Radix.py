from components.creat_list import creatingTheList
from typing import List, Generator, Tuple

def radix_sort(array: List[int]) -> List[int]:
    max_num = max(array)
    exp = 1

    #looping until all digits have been processed
    while max_num // exp > 0:
        array = countingSortByDigit(array, exp)
        exp *= 10

    return array

def countingSortByDigit(array: List[int], exp: int) -> List[int]:
    n = len(array)
    output = [0] * n
    count = [0] * 10

    #counting the occurance of the digit
    for i in range(n):
        digit = (array[i] // exp) % 10
        count[digit] += 1

    #cumulitive counts
    for i in range(1, 10):
        count[i] += count[i - 1]

    #building the output
    for i in range(n - 1, -1, -1):
        digit = (array[i] // exp) % 10
        output[count[digit] - 1] = array[i]
        count[digit] -= 1

    return output

def radix_sort_steps(array: List[int]) -> Generator[Tuple[List[int], int, int], None, None]:
    max_num = max(array)
    exp = 1

    while max_num // exp > 0:
        # Perform counting sort by this digit
        n = len(array)
        output = [0] * n
        count = [0] * 10

        # Step 1: Count occurrences of each digit
        for i in range(n):
            digit = (array[i] // exp) % 10
            count[digit] += 1
            yield (array.copy(), i, exp)  # highlight element being counted

        # Step 2: Cumulative counts
        for i in range(1, 10):
            count[i] += count[i - 1]
            yield (array.copy(), i, exp)  # highlight cumulative update

        # Step 3: Build output (stable)
        for i in range(n - 1, -1, -1):
            digit = (array[i] // exp) % 10
            pos = count[digit] - 1
            output[pos] = array[i]
            count[digit] -= 1
            yield (output.copy(), pos, exp)  # highlight placement

        # Update array for next digit pass
        array = output.copy()
        exp *= 10

        # Final sorted array
    yield (array.copy(), -1, exp)


if __name__ == '__main__':
    num: List[int] = creatingTheList(10)
    num2 = radix_sort(num.copy())
    print(num2)
