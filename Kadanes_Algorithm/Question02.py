# Questions:- 918. Maximum Sum Circular Subarray

# Problem :- Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.


#  Example 1:
# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.


# Example 2:
# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

# Example 3:
# Input: nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2.

# Code :--


def subArrayMaxSum(nums):
    current_max = 0
    sum_max = nums[0]

    current_min = 0
    sum_min = nums[0]

    total_sum = 0

    for num in nums:
        current_max = max(current_max + num, num)
        sum_max = max(sum_max, current_max)

        current_min = min(current_min + num, num)
        sum_min = min(sum_min, current_min)

        total_sum += num

    if sum_max < 0:
        return sum_max

    return max(sum_max, total_sum - sum_min)


nums = [1, -2, 3, -2]
print(subArrayMaxSum(nums))
