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
