#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (51.28%)
# Total Accepted:    316.1K
# Total Submissions: 616.3K
# Testcase Example:  '[1,2,3,1]'
#
# Given an array of integers, find if the array contains any duplicates.
# 
# Your function should return true if any value appears at least twice in the
# array, and it should return false if every element is distinct.
# 
# Example 1:
# 
# 
# Input: [1,2,3,1]
# Output: true
# 
# Example 2:
# 
# 
# Input: [1,2,3,4]
# Output: false
# 
# Example 3:
# 
# 
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true
# 
#














from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)
        return len(numsSet) != len(nums)


"""
# Another approach: sorting
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx-1]:
                return True
        return False
"""

"""
import unittest

class TestContainsDuplicate(unittest.TestCase):
    def test_emptyList(self):
        self.assertEqual(Solution().containsDuplicate([]), False)

    def test_onlyOneElement(self):
        self.assertEqual(Solution().containsDuplicate([0]), False)

    def test_allAreDifferent(self):
        self.assertEqual(Solution().containsDuplicate([1, 2, 3]), False)

    def test_exampleCase1(self):
        self.assertEqual(Solution().containsDuplicate([1,2,3,1]), True)

    def test_exampleCase2(self):
        self.assertEqual(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]), True)

if __name__ == '__main__':
    unittest.main()
"""
