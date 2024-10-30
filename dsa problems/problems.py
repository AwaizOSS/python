import math

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def Pyramid(filler="*"):
    print("works for stars, letters with symmetry")
    n = int(input("enter the number of rows: "))
    for i in range(n):
        for j in range(n - i + 1):
            print(" ", end="")
        # for k in range(2 * i + 1):
        #     if filler != "*":
        #         print(filler[k], end="")
        #     else:
        #         print("*", end="")
        k = 0
        breakpoint = 0
        while k <= 2 * i:
            if filler != "*":
                print(filler[breakpoint], end="")

                if k < i:
                    breakpoint += 1
                else:
                    breakpoint -= 1
            else:
                print("*", end="")
            k += 1
        for l in range(n - i + 1):
            print(" ", end="")
        print("")


def letter_pyramid_gpt():
    n = int(input("Enter the number of rows: "))
    for i in range(n):
        # Print leading spaces
        print(" " * (n - i - 1), end="")

        # Print the first half of the row
        for j in range(i + 1):
            print(chr(65 + j), end="")

        # Print the second half of the row
        for j in range(i - 1, -1, -1):
            print(chr(65 + j), end="")

        # Print trailing spaces and move to the next line
        print(" " * (n - i - 1))


def reverseStarPyramid():
    n = int(input("enter the number of rows: "))
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for k in range(2 * (n - 1 - i) + 1):
            print("*", end="")
        for l in range(i):
            print(" ", end="")
        print("\n")


def defeatMonsters():
    monsters = []
    no_of_monsters = int(input("number of monster: "))
    playerPower = int(input("initial experience/power: "))
    for i in range(no_of_monsters):
        power = input(f"power of monster {i + 1}: ")
        bonus = input(f"bonus of monster {i + 1}: ")
        monsters.append(
            {
                "power": int(power),
                "bonus": int(bonus),
            }
        )
    monsters.sort(key=lambda x: x["power"])
    print(monsters)
    for i in range(no_of_monsters):
        print(playerPower)
        if playerPower >= monsters[i]["power"]:
            print(f"monster {i + 1} defeated")
            playerPower += monsters[i]["bonus"]
        else:
            print(f"monster(s) from {i + 1} cannot be defeated")
            break


# chatgpt solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store the indices of the elements
        num_to_index = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

        return []  # This line will never be reached because there's always one solution


# Example usage:
solution = Solution()
# print(solution.twoSum([2, 7, 11, 15], 9)) Output: [0, 1]


def reverseString(str="123456789"):
    reverse_str = ""
    for i in str:
        reverse_str = (i) + reverse_str
    print(reverse_str)
    # or just reverse_str=str[::-1]


def second_largest_element_from_array(array=[4, 8, 6, 2, 1, 5, 3, 7, 0]):
    # array.sort() changes the original list
    if len(array) > 2:  # always remember the edge cases
        new_array = sorted(array)  # reverse=True can also be passed with array
        print(new_array)
        return new_array[-2]


def second_largest_element_from_array2(array=[4, 8, 6, 2, 1, 5, 3, 7, 0]):
    if len(array) < 2:
        return None  # Handle edge case where there are fewer than 2 elements

    first_largest = second_largest = float("-inf")
    for num in array:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num != first_largest:
            second_largest = num

    return second_largest


def palindrome_check(str="racecar"):
    for i, letter in enumerate(str):
        if letter != str[-i - 1]:
            return False
    return True
    # or else just- return input_string == input_string[::-1]


def tcs1():
    # inputs are T
    # L M
    # b1 b2 b3 ...bM where T is the times we repeat logic, L & M is any number followed by the bx array. We have to output two numbers for each T: 1st the smallest value of |bx+by-L| such that x!=y, 2nd the number of [x,y] pairs that gets the smallest value

    # t = int(input("no of repitions: "))
    arr = []
    smallest_value = float("inf")
    smallest_value_pairs_count = 0
    l_and_m = input("enter l & m separated by a single space: ")
    [lstr, mstr] = l_and_m.split(" ")
    for i in range(int(mstr)):
        arr.append(int(input(f"enter array element {i+1}: ")))

    for i in arr:
        for j in arr:
            if i != j:
                # print(i, j)
                # print("value", abs(i + j - int(lstr)))
                if abs(i + j - int(lstr)) < smallest_value:
                    smallest_value = abs(i + j - int(lstr))
                    smallest_value_pairs_count = 1
                elif abs(i + j - int(lstr)) == smallest_value:
                    smallest_value_pairs_count += 1

    print(smallest_value, smallest_value_pairs_count)


def tcs2():
    # there are three cups with a gem in anyone of them. any two cups are to be shuffled three times and the gem cup needs to be found out. consider the renumbering/reordering of cups when the positions of cups change. output the cup position/number of the cup with the gem
    # inputs are N
    # a b
    # c d
    # e f where N is the intial cup number/position with the gem & [a,b],[c,d],[e,f] are shuffle orders
    a = b = c = False
    cup_list = [a, b, c]
    initial_gem_cup = int(input("enter the initial position of gem: "))
    cup_list[initial_gem_cup - 1] = True
    for i in range(3):
        str = input("enter the cups to be shuffled separated by a single space: ")
        [cup1, cup2] = str.split()
        cup_list[int(cup1) - 1], cup_list[int(cup2) - 1] = (
            cup_list[int(cup2) - 1],
            cup_list[int(cup1) - 1],
        )
    print(cup_list.index(True) + 1)
