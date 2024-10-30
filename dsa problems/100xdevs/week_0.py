# https://projects.100xdevs.com/tracks/dsa/dsa1
def no_of_good_pairs(nums=[1, 2, 3, 1, 1, 3]):
    """
    Given an array of integers nums, return the number of good pairs.
    A pair (i, j) is called good if nums[i] == nums[j] and i < j.

    Constraints:
        1 <= nums.length <= 100
        1 <= nums[i] <= 100

    Example 1:
    Input: nums = [1,2,3,1,1,3]
    Output: 4
    Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

    Args: an array of integers

    Returns: The no. of the good pairs.
    """
    no_of_good_pairs = 0
    for i, num1 in enumerate(nums):
        new_nums = nums[i + 1 :]
        for j, num2 in enumerate(new_nums):
            if num1 == num2:
                no_of_good_pairs += 1
    print(no_of_good_pairs)


def no_of_good_pairs2(nums=[1, 2, 3, 1, 1, 3]):
    no_of_good_pairs = 0
    frequency = [0] * 101  # works only when array isnt supposed too big.
    for i, num1 in enumerate(nums):
        no_of_good_pairs += frequency[nums[i]]
        frequency[nums[i]] += 1

    return no_of_good_pairs


# hw is to determine the pairs using the same approach & to handle negative numbers
