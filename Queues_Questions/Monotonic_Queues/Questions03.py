# Questions :-- 239. Sliding Window Maximum
"""
Problem statements :---

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


Example 2:
Input: nums = [1], k = 1
Output: [1]

"""

# Code :----

import collections


def maxSlindingWindow(nums, k):
    n = len(nums)
    result = []
    deque = collections.deque()

    for i in range(n):
        if deque and deque[0] <= i - k:
            deque.popleft()

        while deque and nums[deque[-1]] <= nums[i]:
            deque.pop()

        deque.append(i)

        if i >= k - 1:
            result.append(nums[deque[0]])

    return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(maxSlindingWindow(nums, k))

