# ID - 97850928

from typing import List


def delivery_service(weights: List[int], limit: int) -> int:
    if len(weights) < 1:
        raise ValueError('Incorrect data')

    if min(weights) >= limit:
        return len(weights)

    weights.sort()
    count: int = 0
    left: int = 0
    right: int = len(weights) - 1

    while left <= right:
        if weights[left] + weights[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        count += 1

    return count


weights = list(map(int, input().split()))
limit = int(input())

print(delivery_service(weights, limit))
