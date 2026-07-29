# Questions :- 152. Maximum Product Subarray
"""
Problem :- Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
Note that the product of an array with a single element is the value of that element.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""

# Code :--


def maxProductArray(nums):
    n = len(nums)

    left_product = 1
    right_product = 1
    ans = nums[0]

    for i in range(n):
        if left_product == 0:
            left_product = 1

        if right_product == 0:
            right_product = 1

        left_product *= nums[i]
        right_product *= nums[n - i - 1]

        ans = max(ans, left_product, right_product)

    return ans


nums = [2, 3, -2, 4]
print(maxProductArray(nums))
