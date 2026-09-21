# Questions :-- 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
"""
Problem Statements :--

Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.


Example 1:
Input: nums = [8,2,4,7], limit = 4
Output: 2

Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.

Example 2:
Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

Example 3:
Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3


"""

# Code :---

from collections import deque


def longestSubArray(nums, limits):
    left = 0
    res = 0
    min_q = deque()
    max_q = deque()

    for right in range(len(nums)):
        while min_q and nums[right] < min_q[-1]:
            min_q.pop()

        while max_q and nums[right] > max_q[-1]:
            max_q.pop()

        min_q.append(nums[right])
        max_q.append(nums[right])

        while max_q[0] - min_q[0] > limits:
            if nums[left] == max_q[0]:
                max_q.popleft()

            if nums[left] == min_q[0]:
                min_q.popleft()

            left += 1

            res = max(res, right - left + 1)

    return res


nums = [8, 2, 4, 7]
limit = 4
print(longestSubArray(nums, limit))
