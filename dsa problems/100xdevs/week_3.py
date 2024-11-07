a = [1, 2, 3, 4, 5]


def nearbySquares(i, sum_b, sum_c):
    """
    You are given an array A of length N. There are two empty arrays, B and C. You have to put every element of A into either B or C. The score of an array is defined as the square of the sum of all of its elements. Find the minimum possible absolute difference between the score of B and C.

    Input Format:
        The first line of input contains a single integer T, denoting the number of test cases.
        The first line of each test case contains a single integer N, denoting the length of the array
        The second line of each test case contains N integers, denoting the elements of array

    Output Format:
        For each test case, print the minimum possible absolute difference between the score of
        and the score of

    Constraints:
        1<=T<=10
        1<=N<=20
        1<=A[i]<=10^8

    Sample Input
        2
        4
        4 5 10 3
        5
        1 3 5 4 5
    Sample Output
        44
        0
    """
    if i == len(a):
        return abs(sum_c**2 - sum_b**2)

    one = nearbySquares(i + 1, sum_b + a[i], sum_c)
    two = nearbySquares(i + 1, sum_b, sum_c + a[i])

    return min(one, two)


import math


def merge_sort(b=[7, 4, 2, 6, 8, 5]):
    def recursion(start, end):
        if start == end:
            return

        mid = math.floor((start + end) / 2)
        recursion(start, mid)
        recursion(mid + 1, end)

        combine(start, mid, end)

    def combine(l, m, n):
        temp = []
        start = l  # Save the original starting index for later

        # Merge two halves into temp
        left_index, right_index = l, m + 1
        while left_index <= m and right_index <= n:
            if b[left_index] <= b[right_index]:  # Sort in ascending order
                temp.append(b[left_index])
                left_index += 1
            else:
                temp.append(b[right_index])
                right_index += 1

        # Append any remaining elements from the left half
        while left_index <= m:
            temp.append(b[left_index])
            left_index += 1

        # Append any remaining elements from the right half
        while right_index <= n:
            temp.append(b[right_index])
            right_index += 1

        # Copy back to b from temp
        for i, value in enumerate(temp):
            b[start + i] = value

    recursion(0, len(b) - 1)
    return b


no_of_ways_to_climb = 0


def staircase(stairs_left):
    """
    You have N stairs in front of you. At every step, you can either climb up by 1, 2 or 3 stairs.
    How many ways are there to climb to the top?
    """

    if stairs_left == 0:
        return 1
    elif stairs_left < 0:
        return 0

    return (
        staircase(stairs_left - 1)
        + staircase(stairs_left - 2)
        + staircase(stairs_left - 3)
    )
