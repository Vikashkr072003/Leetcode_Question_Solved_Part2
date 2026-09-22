# Questions :---- 451. Sort Characters By Frequency
"""
Problem Statement :---

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

"""

# Code :---


def frequencySort(s):
    # Count frequency of each character
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1

    # Create buckets where index = frequency
    buckets = [[] for _ in range(len(s) + 1)]
    for char, count in freq.items():
        buckets[count].append(char)

    # Walk buckets from highest frequency to lowest
    result = []
    for i in range(len(s), 0, -1):
        for char in buckets[i]:
            result.append(char * i)
    return "".join(result)


s = "tree"
print(frequencySort(s))
