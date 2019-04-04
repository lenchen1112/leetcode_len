#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#
# https://leetcode.com/problems/h-index-ii/description/
#
# algorithms
# Medium (35.26%)
# Total Accepted:    77.2K
# Total Submissions: 218.9K
# Testcase Example:  '[0,1,3,5,6]'
#
# Given an array of citations sorted in ascending order (each citation is a
# non-negative integer) of a researcher, write a function to compute the
# researcher's h-index.
# 
# According to the definition of h-index on Wikipedia: "A scientist has index h
# if h of his/her N papers have at least h citations each, and the other N − h
# papers have no more than h citations each."
# 
# Example:
# 
# 
# Input: citations = [0,1,3,5,6]
# Output: 3 
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each
# of them had 
# ⁠            received 0, 1, 3, 5, 6 citations respectively. 
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining 
# two with no more than 3 citations each, her h-index is 3.
# 
# Note:
# 
# If there are several possible values for h, the maximum one is taken as the
# h-index.
# 
# Follow up:
# 
# 
# This is a follow up problem to H-Index, where citations is now guaranteed to
# be sorted in ascending order.
# Could you solve it in logarithmic time complexity?
# 
# 
#


from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        paperCount = len(citations)
        left = 0
        right = paperCount

        while left < right:
            middle = left + (right - left) // 2
            if citations[middle] >= paperCount - middle:
                right = middle # keep this index
            else:
                left = middle + 1 # discard this index

        # left == right, either find the h-index or out of bound
        return paperCount - left if left < paperCount else 0


"""
import unittest


class TestHIndex(unittest.TestCase):
    def test_emptyInput(self):
        self.assertEqual(Solution().hIndex([]), 0)

    def test_onlyOnePaperWithNoCitation(self):
        self.assertEqual(Solution().hIndex([0]), 0)

    def test_multiplePapersButNoCitation(self):
        self.assertEqual(Solution().hIndex([0, 0]), 0)

    def test_onlyOnePaperWithCitations(self):
        self.assertEqual(Solution().hIndex([3]), 1)

    def test_multiplePapersWithCitations1(self):
        self.assertEqual(Solution().hIndex([1, 5]), 1)

    def test_multiplePapersWithCitations2(self):
        self.assertEqual(Solution().hIndex([2, 5]), 2)

    def test_problemExample(self):
        self.assertEqual(Solution().hIndex([0, 1, 3, 5, 6]), 3)

if __name__ == '__main__':
    unittest.main()
"""
