# Question :- 151. Reverse Words in a String

# Problem :- Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


# Code :---


# def reverseWord(str):
#     words = str.split()
#     return " ".join(words[::-1])


# print(reverseWord("the sky is blue"))


# def reverseWords(str):
#     words = str.split()
#     return " ".join(words[::-1])


# print(reverseWords("the sky is blue"))


# -------------------------------------------------

# Code with Two Pointers


def reverseWords(str):
    result = []
    i = len(str) - 1

    while i >= 0:
        # Skip spaces
        while i >= 0 and str[i] == " ":
            i -= 1
        if i < 0:
            break

        # Find start of word
        end = i
        while i >= 0 and str[i] != " ":
            i -= 1

        # Append word to result
        result.append(str[i + 1 : end + 1])

    return " ".join(result)


print(reverseWords("the sky is blue"))


