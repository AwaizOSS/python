# https://projects.100xdevs.com/tracks/dsa2/dsa-1


def highest_altitude(gain=[-5, 1, 5, 0, -7]):
    """
    There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

    You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

    Constraints:
        n == gain.length
        1 <= n <= 100
        -100 <= gain[i] <= 100

    Example 1:
    Input: gain = [-5,1,5,0,-7]
    Output: 1
    Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
    """

    highest_alt = 0
    alt = [0] * (len(gain) + 1)

    for i, g in enumerate(gain):
        alt[i + 1] = g + alt[i]
        if alt[i + 1] > highest_alt:
            highest_alt = alt[i + 1]

    return highest_alt


def highest_altitude_chatgpt(gain=[-5, 1, 5, 0, -7]):
    highest_alt = 0
    current_alt = 0

    for g in gain:
        current_alt += g
        highest_alt = max(highest_alt, current_alt)

    return highest_alt


# Given a string containing lower case english alphabets, what is the most occurring character?

# Example 1:
# Input: s = "hello"
# Output: l
# Explanation: Frequencies - 'h': 1, 'e': 1, 'l': 2, 'o': 1


# for this we convert hello into integer by using ascii values which is done as ord('h')-ord('a') for lower case with 26 array size, ord('A') for upper case, ord('0') for string numbers with array size 10 & use direct ascii values from ord(...) for all mixed chcracter i.e., if string includes lower case, upper case, number strings & special characters with 256 array size


def max_population_year(logs=[[1950, 1961], [1970, 1981], [1960, 1971]]):
    """
    You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.

    The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.

    Return the earliest year with the maximum population.

    Constraints:
        1 <= logs.length <= 100
        1950 <= birthi < deathi <= 2050

    Example 1:
    Input: logs = [[1993,1999],[2000,2010]]
    Output: 1993
    Explanation: The maximum population is 1, and 1993 is the earliest year with this population.

    Example 2:
    Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
    Output: 1960
    Explanation:
    The maximum population is 2, and it had happened in years 1960 and 1970.
    The earlier year between them is 1960.
    """

    gain = [0] * 101
    for [birth, death] in logs:
        gain[birth - 1950] += 1
        gain[death - 1950] -= 1

    max_population = gain[0]
    max_population_year = 0
    freq = [0] * (len(gain) + 1)
    for i, g in enumerate(gain):
        freq[i + 1] = g + freq[i]
        if max_population < freq[i + 1]:
            max_population = freq[i + 1]
            max_population_year = i + 1950

    print(max_population, max_population_year)


max_population_year()
