# Questions :--- 1696.Jump Game VI
"""
Problem Statements :---

You are given a 0-indexed integer array nums and an integer k.
You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.
Return the maximum score you can get.

Example 1:
Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7

Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.


Example 2:
Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17

Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.

"""

# Code :--

# import collections


# def maxResult(nums, k):
#     n = len(nums)
#     dp = [0] * n
#     dp[0] = nums[0]
#     # Monotonic deque storing indices, dp values in decreasing order
#     dq = collections.deque([0])

#     for i in range(1, n):
#         # Remove indices outside the jump window
#         while dq and dq[0] < i - k:
#             dq.popleft()

#         # Front has the max dp value in the window
#         dp[i] = nums[i] + dp[dq[0]]

#         # Maintain decreasing order: remove smaller dp values from back
#         while dq and dp[dq[-1]] <= dp[i]:
#             dq.pop()
#         dq.append(i)

#     return dp[n - 1]


# nums = [1, -5, -20, 4, -1, 3, -6, -3]
# k = 2
# print(maxResult(nums, k))


import collections


def maxResult(nums, k):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]

    dq = collections.deque([0])

    for i in range(1, n):
        while dq and dq[0] < i - k:
            dq.popleft()

        dp[i] = nums[i] + dp[dq[0]]

        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()
        dq.append(i)

    return dp[n - 1]


nums = [1, -5, -20, 4, -1, 3, -6, -3]
k = 2

print(maxResult(nums, k))
