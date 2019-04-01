#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array/description/
#
# algorithms
# Easy (29.32%)
# Total Accepted:    277K
# Total Submissions: 944.7K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# Given an array, rotate the array to the right by k steps, where k is
# non-negative.
# 
# Example 1:
# 
# 
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# 
# 
# Note:
# 
# 
# Try to come up as many solutions as you can, there are at least 3 different
# ways to solve this problem.
# Could you do it in-place with O(1) extra space?
# 
#

from typing import List


class Solution:
    def reverseNumsInPlace(self, nums, startIdx, stopIdx):
        sliceLength = (stopIdx - startIdx + 1) // 2
        for i in range(sliceLength):
            nums[startIdx + i], nums[stopIdx - i] = nums[stopIdx - i], nums[startIdx + i]

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None

        n = k % len(nums)
        if not n:
            return None

        self.reverseNumsInPlace(nums, 0, len(nums) - 1)
        self.reverseNumsInPlace(nums, 0, n - 1)
        self.reverseNumsInPlace(nums, n, len(nums) - 1)


"""
import unittest


class TestReverseNumsInPlace(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 2, 3, 4, 5]
        Solution().reverseNumsInPlace(nums, 0, 2)
        self.assertEqual(nums, [3, 2, 1, 4, 5])
    
    def test_case_2(self):
        nums = [1, 2, 3, 4, 5]
        Solution().reverseNumsInPlace(nums, 0, 3)
        self.assertEqual(nums, [4, 3, 2, 1, 5])

class TestRotate(unittest.TestCase):
    def test_emptyList(self):
        nums = []
        Solution().rotate(nums, 1)
        self.assertEqual(nums, nums)

    def test_rotateZero(self):
        nums = [1, 2]
        Solution().rotate(nums, 0)
        self.assertEqual(nums, nums)

    def test_rotateMoreThanLength(self):
        nums = [1, 2, 3]
        Solution().rotate(nums, 4)
        self.assertEqual(nums, [3, 1, 2])

    def test_oridinaryCase(self):
        nums = [1, 2, 3, 4]
        Solution().rotate(nums, 2)
        self.assertEqual(nums, [3, 4, 1, 2])

if __name__ == '__main__':
    unittest.main()
"""
