#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (31.52%)
# Total Accepted:    248.5K
# Total Submissions: 787.1K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
#
# Each element in the array represents your maximum jump length at that
# position.
#
# Determine if you are able to reach the last index.
#
# Example 1:
#
#
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum
# jump length is 0, which makes it impossible to reach the last index.
#
#
#


from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex = 0
        for idx, num in enumerate(nums):
            if idx > maxIndex:
                return False
            maxIndex = max(maxIndex, idx + num)
        return True


"""
import unittest


class TestCanJump(unittest.TestCase):
    def test_emptyList(self):
        self.assertEqual(Solution().canJump([]), True)

    def test_onlyOneElement(self):
        self.assertEqual(Solution().canJump([0]), True)

    def test_pathBreakInTheMiddle(self):
        self.assertEqual(Solution().canJump([2, 3, 1, 1, 0, 5, 8]), False)

    def test_example1(self):
        self.assertEqual(Solution().canJump([2, 3, 1, 1, 4]), True)

    def test_example2(self):
        self.assertEqual(Solution().canJump([3, 2, 1, 0, 4]), False)


if __name__ == '__main__':
    unittest.main()
"""
