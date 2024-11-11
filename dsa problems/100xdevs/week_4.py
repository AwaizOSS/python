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


def countPairs(nums=[1, 3, 4, 6, 8, 9], target=17):
    """
    Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j)
    where 0 <= i < j < n and nums[i] + nums[j] < target.


    Example 1:
        Input: nums = [-1,1,2,3,1], target = 2
        Output: 3
        Explanation: There are 3 pairs of indices that satisfy the conditions in the statement:
            - (0, 1) since 0 < 1 and nums[0] + nums[1] = 0 < target
            - (0, 2) since 0 < 2 and nums[0] + nums[2] = 1 < target
            - (0, 4) since 0 < 4 and nums[0] + nums[4] = 0 < target
        Note that (0, 3) is not counted since nums[0] + nums[3] is not strictly less than the target.

    Example 2:
        Input: nums = [-6,2,5,-2,-7,-1,3], target = -2
        Output: 10
        Explanation: There are 10 pairs of indices that satisfy the conditions in the statement:
            - (0, 1) since 0 < 1 and nums[0] + nums[1] = -4 < target
            - (0, 3) since 0 < 3 and nums[0] + nums[3] = -8 < target
            - (0, 4) since 0 < 4 and nums[0] + nums[4] = -13 < target
            - (0, 5) since 0 < 5 and nums[0] + nums[5] = -7 < target
            - (0, 6) since 0 < 6 and nums[0] + nums[6] = -3 < target
            - (1, 4) since 1 < 4 and nums[1] + nums[4] = -5 < target
            - (3, 4) since 3 < 4 and nums[3] + nums[4] = -9 < target
            - (3, 5) since 3 < 5 and nums[3] + nums[5] = -3 < target
            - (4, 5) since 4 < 5 and nums[4] + nums[5] = -8 < target
            - (4, 6) since 4 < 6 and nums[4] + nums[6] = -4 < target


    Constraints:
        1 <= nums.length == n <= 50
        -50 <= nums[i], target <= 50
    """
    nums.sort()  # Sort the array to use binary search
    condition_matching_pairs = 0

    for i in range(len(nums) - 1):
        low, high = i + 1, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            # Check if nums[i] + nums[mid] is less than the target
            if nums[i] + nums[mid] < target:
                # All pairs from (i, low) to (i, mid) are valid
                condition_matching_pairs += mid - low + 1
                low = mid + 1  # Move right to find more pairs
            else:
                high = mid - 1  # Move left to reduce the sum

    return condition_matching_pairs


def findPeakElement(nums):
    """
    A peak element is an element that is strictly greater than its neighbors.

    Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

    You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

    You must write an algorithm that runs in O(log n) time.

    Example 1:
    Input: nums = [1,2,3,1]
    Output: 2
    Explanation: 3 is a peak element and your function should return the index number 2.

    Example 2:
    Input: nums = [1,2,1,3,5,6,4]
    Output: 5
    Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.


    Constraints:
    1 <= nums.length <= 1000
    -231 <= nums[i] <= 231 - 1
    nums[i] != nums[i + 1] for all valid i.
    """
    l = 0
    h = len(nums) - 1
    if len(nums) == 1:
        return 0

    if nums[l] > nums[l + 1]:
        return l
    elif nums[h] > nums[h - 1]:
        return h

    while l <= h:
        m = math.floor((l + h) / 2)

        if nums[m] > nums[m + 1] and nums[m] > nums[m - 1]:
            return m
        elif nums[m] > nums[m + 1]:
            h = m
        else:
            l = m
