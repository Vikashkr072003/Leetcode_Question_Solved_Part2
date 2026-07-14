# Questions :- 525. Contiguous Array

# Problem :- Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

# Example 1:
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

# Example 2:
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

# Example 3:
# Input: nums = [0,1,1,1,1,1,0,0,0]
# Output: 6
# Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and


# Code :---Approach 1: Brute Force


def maxArrayFind(nums):
    max_len = 0

    for i in range(len(nums)):
        zero = 0
        ones = 0

        for j in range(i, len(nums)):
            if nums[j] == 0:
                zero += 1

            else:
                ones += 1

            if zero == ones:
                max_len = max(max_len, j - i + 1)

    return max_len


nums = [0, 1]
print(maxArrayFind(nums))
