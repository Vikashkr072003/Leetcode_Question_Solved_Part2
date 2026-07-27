# Questions :- 53. Maximum Subarray
# Problem :- Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.


# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.


# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

# Code :-


def maxArraySum(nums):
    current_max = nums[0]
    sum_max = nums[0]

    for i in range(1, len(nums)):
        current_max = max(nums[i], current_max + nums[i])
        sum_max = max(sum_max, current_max)

    return sum_max


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxArraySum(nums))
