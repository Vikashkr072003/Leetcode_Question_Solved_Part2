# Questions :--316. Remove Duplicate Letters
"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"

"""

# Code : -----


def removeDuplicateLetter(str):
    last_index = {}
    for i, ch in enumerate(str):
        last_index[ch] = i

    in_stack = set()
    stack = []

    for i, ch in enumerate(str):
        if ch in in_stack:
            continue

        while stack and stack[-1] > ch and last_index[stack[-1]] > i:
            in_stack.remove(stack.pop())

        stack.append(ch)
        in_stack.add(ch)

    return "".join(stack)


s = "bcabc"
print(removeDuplicateLetter(s))
