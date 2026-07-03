# Question :-- 205. Isomorphic Strings

# Problem :-  Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Explanation:
# The strings s and t can be made identical by:
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.

# Example 2:
# Input: s = "f11", t = "b23"
# Output: false
# Explanation:
# The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

# Example 3:
# Input: s = "paper", t = "title"
# Output: true

#  Code :---


def isIsomorphic(s, t):
    map_st = {}
    map_ts = {}

    for char_s, char_t in zip(s, t):
        if char_s in map_st and map_st[char_s] != char_t:
            return False

        if char_t in map_ts and map_ts[char_t] != char_s:
            return False

        map_st[char_s] = char_t
        map_ts[char_t] = char_s

    return True


s = "bada"
t = "baba"

print(isIsomorphic(s, t))
