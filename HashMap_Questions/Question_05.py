# Questions :--- 219. Contains Duplicate II
# Problem :- Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

# Code :---


# def containDuplicates(nums, k):
#     for i in range(len(nums)):
#         for j in range(max(0, i - k), i):
#             if nums[i] == nums[j]:
#                 return True

#     return False


# nums = [1, 2, 3, 1]
# k = 3
# print(containDuplicates(nums, k))


def containDuplicates(nums, k):
    hashMap = {}

    for i, num in enumerate(nums):

        if num in hashMap:
            if i - hashMap[num] <= k:
                return True
        hashMap[num] = i
    return False


nums = [1, 2, 3, 1]
k = 3

print(containDuplicates(nums, k))
