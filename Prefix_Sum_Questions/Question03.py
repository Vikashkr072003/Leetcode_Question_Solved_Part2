# Questions :- 974. Subarray Sums Divisible by K
# Problem :- Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
# A subarray is a contiguous part of an array.

# Example 1:
# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]


# Example 2:
# Input: nums = [5], k = 9
# Output: 0

# Code :--


def subArrayDiv(nums, k):
    count = 0
    prefix_sum = 0
    remainder_count = {0: 1}

    for num in nums:
        prefix_sum += num
        remainder = prefix_sum % k

        count += remainder_count.get(remainder, 0)
        remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

    return count


nums = [4, 5, 0, -2, -3, 1]
k = 5

print(subArrayDiv(nums, k))
