# Question : 392. Is Subsequence

# Problem :- Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# ---------------

# Code :--


def Subsequence(str1, str2):
    j = 0
    i = 0

    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i += 1
            j += 1

        else:
            j += 1

    return i == len(str1)


print(Subsequence("abc", "ahdbc"))
