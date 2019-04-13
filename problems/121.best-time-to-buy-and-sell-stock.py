#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (46.66%)
# Total Accepted:    469.1K
# Total Submissions: 1M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
# 
# If you were only permitted to complete at most one transaction (i.e., buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.
# 
# Note that you cannot sell a stock before you buy one.
# 
# Example 1:
# 
# 
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
# 
# 
# Example 2:
# 
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
# 
#


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxValue = 0
        lowIdx = 0
        highIdx = 0
        for idx, price in enumerate(prices):
            lowPrice = prices[lowIdx]
            highPrice = prices[highIdx]
            if price < lowPrice:
                maxValue = max(maxValue, highPrice - lowPrice)
                lowIdx = idx
                highIdx = idx
            elif prices[idx] > highPrice:
                highIdx = idx
        return max(maxValue, prices[highIdx] - prices[lowIdx]) if len(prices) else 0


"""
# Another approach: Kadane's Algorithm
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentProfit = 0
        mostProfit = 0
        for idx in range(1, len(prices)):
            currentProfit = max(0, currentProfit + prices[idx] - prices[idx-1])
            mostProfit = max(mostProfit, currentProfit)
        return mostProfit
"""

"""
import unittest

class TestMaxProfit(unittest.TestCase):
    def test_emptyList(self):
        self.assertEqual(Solution().maxProfit([]), 0)

    def test_onlyOneDay(self):
        self.assertEqual(Solution().maxProfit([2]), 0)

    def test_allTheSamePrice(self):
        self.assertEqual(Solution().maxProfit([2, 2, 2]), 0)

    def test_positiveExample1(self):
        self.assertEqual(Solution().maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_positiveExample2(self):
        self.assertEqual(Solution().maxProfit([8, 4, 6, 2, 10]), 8)

    def test_positiveExample3(self):
        self.assertEqual(Solution().maxProfit([8, 4, 6, 2, 1]), 2)

    def test_positiveExample4(self):
        self.assertEqual(Solution().maxProfit([1, 2, 3, 4, 5]), 4)

    def test_negativeExample(self):
        self.assertEqual(Solution().maxProfit([7, 6, 4, 3, 1]), 0)

if __name__ == '__main__':
    unittest.main()
"""
