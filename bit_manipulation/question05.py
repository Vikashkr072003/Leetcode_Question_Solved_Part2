# Question  :- 201. Bitwise AND of Numbers Range
# Problem :- Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.
# Example 1:
# Input: left = 5, right = 7
# Output: 4

# Example 2:
# Input: left = 0, right = 0
# Output: 0

# Example 3:
# Input: left = 1, right = 2147483647
# Output: 0


# Code :- Approach 1: Brute Force


# def rnageBit(left, right):
#     result = left

#     for i in range(left, right):
#         result &= i + 1


#         if result == 0:
#             return 0

#     return result


# print(rnageBit(5, 7))


# Code :- Approach 2: Bit Manipulation


def rangeBit(left, right):
    shifts = 0

    while left != right:
        left >>= 1
        right >>= 1
        shifts += 1

    return shifts


print(rangeBit(5, 7))
