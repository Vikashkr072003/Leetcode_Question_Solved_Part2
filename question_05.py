# Question :--  Zigzag Conversion

# Problem :- The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);


# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"


# Code : --


# def convert(str, numRows):
#     if numRows == 1 or numRows >= len(str):
#         return str

#     rows = [[] for _ in range(numRows)]
#     current_row = 0
#     direction = 1

#     for ch in str:
#         rows[current_row].append(ch)

#         if current_row == 0:
#             direction = 1

#         elif current_row == numRows - 1:
#             direction = -1

#         current_row += direction

#     return "".join("".join(row) for row in rows)


# print(convert("ABCDEFGHIJKLMNOP", 2))


def convert(str, numRows):
    if numRows == 1 or numRows >= len(str):
        return str

    rows = [[] for _ in range(numRows)]
    currnet_rows = 0
    direction = 1

    for ch in str:
        rows[currnet_rows].append(ch)
        if currnet_rows == 0:
            direction = 1

        elif currnet_rows == numRows - 1:
            direction = -1

        currnet_rows += direction
    return "".join("".join(row) for row in rows)


print(convert("ABCDEFGHIJKLMNOP", 5))
