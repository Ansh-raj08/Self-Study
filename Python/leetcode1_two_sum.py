"""LeetCode 1: Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index

        for i, num in enumerate(nums):
            needed = target - num
            if needed in seen:
                return [seen[needed], i]
            seen[num] = i

        # LeetCode guarantees one valid answer, but this keeps the function safe.
        return []


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))   # [0, 1]
    print(s.twoSum([3, 2, 4], 6))        # [1, 2]
    print(s.twoSum([3, 3], 6))           # [0, 1]