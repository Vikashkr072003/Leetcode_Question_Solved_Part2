# Question :--  Counting Bits
# Problem :---Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.


#  Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101


# Code :----------------- Approach 1: Brute Force (Count Bits Individually)


def countBits(nums):
    ans = [0] * (nums + 1)

    for i in range(nums + 1):
        count = 0
        num = i

        while num > 0:
            count += num & 1
            num >>= 1

        ans[i] = count

    return ans


print(countBits(2))


# ------Code :- Approach 2: DP with Right Shift


# def countBits(nums):
#     ans = [0] * (nums + 1)

#     for i in range(1, nums + 1):
#         ans[i] = ans[i >> 1] + (i & 1)

#     return ans


# print(countBits(2))
