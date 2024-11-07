import math


def twoSum(arr=[2, 3, 4, 5, 8, 9], sum=8):
    """
    You are given an array of N elements, and also a number k.
    Find if there are 2 elements, whose sum is equal to k.
    """
    for i in arr:
        target = sum - i
        return bs(target)

    def bs(target):
        low = 0
        high = len(arr) - 1
        mid = abs((low + high) / 2)

        while low <= high:
            if target == mid:
                return True
            elif target > mid:
                low = mid + 1
            else:
                high = mid - 1

        return False


def countPairs(nums=[1, 3, 4, 6, 8, 9], target=12):
    condition_matching_pairs = 0

    for i, num in enumerate(nums):
        otherNumber = target - 1 - num
        low = i + 1  # i<j
        high = len(nums) - 1
        mid = math.floor((low + high) / 2)

        while low <= high:
            if mid == otherNumber:
                condition_matching_pairs += 1
                high = mid - 1
            elif mid > otherNumber:
                high = mid - 1
            else:
                high -= 1
    return condition_matching_pairs


print(countPairs())
