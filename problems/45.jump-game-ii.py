#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (27.70%)
# Total Accepted:    161.1K
# Total Submissions: 580.8K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
#
# Each element in the array represents your maximum jump length at that
# position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example:
#
#
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# ⁠   Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Note:
#
# You can assume that you can always reach the last index.
#
#


from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        currentEnd = 0
        currentMax = 0
        for i in range(len(nums)-1):
            currentMax = max(currentMax, i + nums[i])
            if i == currentEnd:
                jumps += 1
                currentEnd = currentMax
        return jumps


"""
import unittest


class TestJump(unittest.TestCase):
    def test_emptyList(self):
        self.assertEqual(Solution().jump([]), 0)

    def test_onlyOneElement(self):
        self.assertEqual(Solution().jump([0]), 0)

    def test_example1(self):
        self.assertEqual(Solution().jump([2, 3, 1, 1, 4]), 2)

    def test_example2(self):
        self.assertEqual(Solution().jump(
            [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]), 3)


if __name__ == '__main__':
    unittest.main()
"""
