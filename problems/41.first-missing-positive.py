#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (28.45%)
# Total Accepted:    199K
# Total Submissions: 699.6K
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
#
# Input: [1,2,0]
# Output: 3
#
#
# Example 2:
#
#
# Input: [3,4,-1,1]
# Output: 2
#
#
# Example 3:
#
#
# Input: [7,8,9,11,12]
# Output: 1
#
#
# Note:
#
# Your algorithm should run in O(n) time and uses constant extra space.
#
#

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for idx in range(n):
            if nums[idx] <= 0:
                nums[idx] = n + 1
        for idx in range(n):
            target = abs(nums[idx])
            if target <= n:
                nums[target-1] = -abs(nums[target-1])
        for idx in range(n):
            if nums[idx] > 0:
                return idx + 1
        return n + 1


"""
import unittest


class TestFistMissingPositive(unittest.TestCase):
    def test_emptyNums(self):
        self.assertEqual(Solution().firstMissingPositive([]), 1)

    def test_allNonePositive(self):
        self.assertEqual(Solution().firstMissingPositive([-1, -2, 0, -3]), 1)

    def test_negativeAndPositive(self):
        self.assertEqual(Solution().firstMissingPositive([-1, 0, 1, 3]), 2)

    def test_allPositive1(self):
        self.assertEqual(Solution().firstMissingPositive([4, 9, 5]), 1)

    def test_allPositive2(self):
        self.assertEqual(Solution().firstMissingPositive([2, 5, 1]), 3)

    def test_allPositive3(self):
        self.assertEqual(Solution().firstMissingPositive([3, 4, -1, 1]), 2)

    def test_duplicateElements(self):
        self.assertEqual(Solution().firstMissingPositive([1, 1]), 2)

    def test_allConsecutive(self):
        self.assertEqual(Solution().firstMissingPositive([1, 3, 2, 4, 5]), 6)


if __name__ == '__main__':
    unittest.main()
"""
