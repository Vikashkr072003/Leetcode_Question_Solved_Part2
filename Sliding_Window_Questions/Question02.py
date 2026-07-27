# Questions :- 567. Permutation in String
# Problem :- Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").


# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false


# Code :----


def checkInclusion(s1, s2):
    n = len(s1)
    m = len(s2)

    if n > m:
        return False

    s1_freq = [0] * 26
    window_freq = [0] * 26

    for i in range(n):
        s1_freq[ord(s1[i]) - ord("a")] += 1
        window_freq[ord(s2[i]) - ord("a")] += 1

    if s1_freq == window_freq:
        return True

    for i in range(n, m):
        window_freq[ord(s2[i]) - ord("a")] += 1
        window_freq[ord(s2[i - n]) - ord("a")] -= 1

        if s1_freq == window_freq:
            return True

    return False


s1 = "ab"

s2 = "eidboaoo"

print(checkInclusion(s1, s2))
