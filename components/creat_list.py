import random
from typing import List

def creatingTheList(n: int) -> List[int]:
    numbers = []
    for i in range(n):
        num: int = random.randint(1, n)
        if num not in numbers:
            numbers.append(num)
        else:
            while True:
                num = random.randint(1, n)
                if num not in numbers:
                    numbers.append(num)
                    break
    print(numbers)
    return numbers