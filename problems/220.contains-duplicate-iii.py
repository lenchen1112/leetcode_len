#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#
# https://leetcode.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (19.54%)
# Total Accepted:    88.3K
# Total Submissions: 452.1K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# Given an array of integers, find out whether there are two distinct indices i
# and j in the array such that the absolute difference between nums[i] and
# nums[j] is at most t and the absolute difference between i and j is at most
# k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false
# 
# 
# 
# 
# 
#




from typing import List
from collections import OrderedDict


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 1 or t < 0:
            return False
        orderedDict = OrderedDict()
        for num in nums:
            quotient = num if not t else num // t
            candidates = (orderedDict.get(quotient-1), orderedDict.get(quotient), orderedDict.get(quotient+1))
            for candidate in candidates:
                if candidate is not None and abs(num-candidate) <= t:
                    return True
            if len(orderedDict) == k:
                orderedDict.popitem(last=False)
            orderedDict[quotient] = num
        return False

"""
import unittest

class TestContainsNearbyAlmostDuplicate(unittest.TestCase):
    def test_emptyList(self):
        self.assertEqual(Solution().containsNearbyAlmostDuplicate([], 2, 2), False)

    def test_kIsLargerThanLength(self):
        self.assertEqual(Solution().containsNearbyAlmostDuplicate([1, 2], 3, 2), True)

    def test_example1(self):
        self.assertEqual(Solution().containsNearbyAlmostDuplicate([1,2,3,1], 3, 0), True)

    def test_example2(self):
        self.assertEqual(Solution().containsNearbyAlmostDuplicate([1,0,1,1], 1, 2), True)

    def test_example3(self):
        self.assertEqual(Solution().containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3), False)

    def test_memoryIssue(self):
        self.assertEqual(Solution().containsNearbyAlmostDuplicate([0,2147483647], 1, 2147483647), True)


if __name__ == '__main__':
    unittest.main()
"""
