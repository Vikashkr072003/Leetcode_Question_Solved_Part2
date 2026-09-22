# Questions :--- 692. Top K Frequent Words
"""
Problem Statement :----


Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

Example 1:
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

"""

# Code :---


def topKFrequent(nums, k):
    count = {}

    for num in nums:
        count[num] = count.get(num, 0) + 1

    buckets = [[] for __ in range(len(nums) + 1)]

    for num, freq in count.items():
        buckets[freq].append(num)

    result = []

    for freq in range(len(nums), 0, -1):
        for num in buckets[freq]:
            result.append(num)

            if len(result) == k:
                return result

    return result


nums = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(topKFrequent(nums, k))
