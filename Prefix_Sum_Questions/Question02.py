# Questions :- 560. Subarray Sum Equals K
# Problem :- Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.


# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:
# Input: nums = [1,2,3], k = 3
# Output:

# Code :-- Approach :- Prefix Sum + Hash Map


def subArray(nums, k):
    count = 0
    prefix_sum = 0
    prefix_count = {0: 1}

    for num in nums:
        prefix_sum += num
        count += prefix_count.get(prefix_sum - k, 0)
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

    return count


nums = [1, 1, 1]
k = 2
print(subArray(nums, k))
