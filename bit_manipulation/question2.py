# Questions :- 191. Number of 1 Bits

# Problem :- Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

# Example 1:

# Input: n = 11

# Output: 3

# Explanation:

# The input binary string 1011 has a total of three set bits.

# Example 2:

# Input: n = 128

# Output: 1

# Explanation:

# The input binary string 10000000 has a total of one set bit.

# Example 3:

# Input: n = 2147483645

# Output: 30

# Explanation:

# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.


# Coode :-------

# Method : 1 Approach 1: Check Each Bit


def oneSingle(num):

    result = 0

    while num:
        result += num % 2
        num = num >> 1
    return result


print(oneSingle(2147483645))


# Method Second :- Approach 2: Brian Kernighan's Algorithm


def oneSingle(num):

    result = 0

    while num:
        num = num & (num - 1)  # num &= (num - 1)
        result += 1

    return result


print(oneSingle(11))
