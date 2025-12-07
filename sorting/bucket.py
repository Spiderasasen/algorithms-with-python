from components.creat_list import creatingTheList
from typing import List, Generator, Tuple

def bucket_sort(array: List[int]) -> List[int]:
    n = len(array)
    if n == 0:
        return array

    # Step 1: Find max value to normalize
    max_val = max(array)

    # Step 2: Create buckets
    buckets = [[] for _ in range(n)]

    # Step 3: Distribute elements into buckets
    for num in array:
        index = (num * (n - 1)) // max_val   # scale into [0, n-1]
        buckets[index].append(num)

    # Step 4: Sort each bucket
    for bucket in buckets:
        bucket.sort()

    # Step 5: Concatenate buckets
    output = []
    for bucket in buckets:
        output.extend(bucket)

    return output


def bucket_sort_steps(array: List[float]) -> Generator[Tuple[List[float], int, List[List[float]]], None, None]:
    n = len(array)
    if n == 0:
        return

    min_val = min(array)
    max_val = max(array)
    if max_val == min_val:
        # All elements equal — single bucket and immediate output
        buckets = [array.copy()] + [[] for _ in range(n - 1)]
        yield (array.copy(), -1, buckets)
        yield (array.copy(), -1, buckets)
        yield (array.copy(), -1, buckets)
        yield (array.copy(), -1, buckets)
        return

    buckets: List[List[float]] = [[] for _ in range(n)]

    # Step 1: Distribute elements into buckets (scale into [0, n-1])
    for idx, num in enumerate(array):
        ratio = (num - min_val) / (max_val - min_val)
        index = min(n - 1, int(ratio * n))  # clamp to avoid n
        buckets[index].append(num)
        yield (array.copy(), idx, [b.copy() for b in buckets])

    # Step 2: Sort each bucket
    for b_idx, bucket in enumerate(buckets):
        bucket.sort()
        yield (array.copy(), b_idx, [b.copy() for b in buckets])

    # Step 3: Concatenate buckets
    output: List[float] = []
    for b_idx, bucket in enumerate(buckets):
        output.extend(bucket)
        yield (output.copy(), b_idx, [b.copy() for b in buckets])

    # Final sorted array
    yield (output.copy(), -1, [b.copy() for b in buckets])


if __name__ == '__main__':
    num: List[int] = creatingTheList(10)
    num2: List[int] = bucket_sort(num.copy())
    print(num2)
