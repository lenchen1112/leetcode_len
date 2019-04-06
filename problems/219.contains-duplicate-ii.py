#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (34.93%)
# Total Accepted:    189.1K
# Total Submissions: 541.2K
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an array of integers and an integer k, find out whether there are two
# distinct indices i and j in the array such that nums[i] = nums[j] and the
# absolute difference between i and j is at most k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1], k = 3
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1], k = 1
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
# 
# 
# 
# 
# 
#


from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexMap = {}
        for idx, num in enumerate(nums):
            if num in indexMap and idx - indexMap[num] <= k:
                return True
            indexMap[num] = idx
        return False


"""
import unittest

class TestContainsNearbyDuplicate(unittest.TestCase):
    def test_emptyList(self):
        self.assertEqual(Solution().containsNearbyDuplicate([], 2), False)

    def test_allAreDifferent(self):
        self.assertEqual(Solution().containsNearbyDuplicate([1, 2, 3], 2), False)

    def test_kIsLargerThanNumsLen(self):
        self.assertEqual(Solution().containsNearbyDuplicate([1, 2], 3), False)

    def test_exampleCase1(self):
        self.assertEqual(Solution().containsNearbyDuplicate([1,2,3,1], 3), True)

    def test_exampleCase2(self):
        self.assertEqual(Solution().containsNearbyDuplicate([1,0,1,1], 1), True)

    def test_exampleCase3(self):
        self.assertEqual(Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2), False)

if __name__ == '__main__':
    unittest.main()
"""
