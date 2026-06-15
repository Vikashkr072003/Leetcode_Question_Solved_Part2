# Question :-  136. Single Number

# Problem :- Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

# Code :-----------------

# Method First(1) :-- XOR Method:---


# def singleNumber(nums):
#     result = 0

#     for num in nums:
#         result ^= num

#     return result


# arr = [1, 1, 2, 2, 3]
# print(singleNumber(arr))


#  Method Second(2) :-----


def singleNumber(nums):

    hash_map = {}

    for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1

    for k in hash_map:
        if hash_map[k] == 1:
            return k

    return -1


arr = [1, 2, 3, 4, 4, 4]
print(singleNumber(arr))
