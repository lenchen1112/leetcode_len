#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#
# https://leetcode.com/problems/min-cost-climbing-stairs/description/
#
# algorithms
# Easy (46.48%)
# Total Accepted:    73.3K
# Total Submissions: 157.4K
# Testcase Example:  '[0,0,0,0]'
#
#
# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0
# indexed).
#
# Once you pay the cost, you can either climb one or two steps. You need to
# find minimum cost to reach the top of the floor, and you can either start
# from the step with index 0, or the step with index 1.
#
#
# Example 1:
#
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the
# top.
#
#
#
# Example 2:
#
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping
# cost[3].
#
#
#
# Note:
#
# cost will have a length in the range [2, 1000].
# Every cost[i] will be an integer in the range [0, 999].
#
#
#


from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stairsLength = len(cost)
        for idx in range(2, stairsLength):
            cost[idx] = min(cost[idx-1], cost[idx-2]) + cost[idx]
        return min(cost[stairsLength-1], cost[stairsLength-2])


"""
import unittest


class TestMinCostClimbingStairs(unittest.TestCase):
    def test_allZeros(self):
        self.assertEqual(Solution().minCostClimbingStairs([0, 0, 0, 0]), 0)

    def test_example1(self):
        self.assertEqual(Solution().minCostClimbingStairs([10, 15, 20]), 15)

    def test_example2(self):
        self.assertEqual(Solution().minCostClimbingStairs(
            [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)


if __name__ == '__main__':
    unittest.main()
"""
