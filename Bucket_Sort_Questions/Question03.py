# Questions :-- 164. Maximum Gap
"""
Problem Statement :---

"""


# Code :--
def maximumGap(nums):
    n = len(nums)
    if n < 2:
        return 0

    lo, hi = min(nums), max(nums)
    if lo == hi:
        return 0

    # Bucket width: at least 1 to avoid division by zero
    bucket_size = max(1, (hi - lo) // (n - 1))
    bucket_count = (hi - lo) // bucket_size + 1

    # Track min and max for each bucket
    bucket_min = [float("inf")] * bucket_count
    bucket_max = [float("-inf")] * bucket_count
    used = [False] * bucket_count

    # Place each element into its bucket
    for num in nums:
        idx = (num - lo) // bucket_size
        used[idx] = True
        bucket_min[idx] = min(bucket_min[idx], num)
        bucket_max[idx] = max(bucket_max[idx], num)

    # Scan buckets to find maximum gap
    max_gap = 0
    prev_max = lo
    for i in range(bucket_count):
        if not used[i]:
            continue
        max_gap = max(max_gap, bucket_min[i] - prev_max)
        prev_max = bucket_max[i]
    return max_gap


nums = [3, 6, 9, 1]
print(maximumGap(nums))
