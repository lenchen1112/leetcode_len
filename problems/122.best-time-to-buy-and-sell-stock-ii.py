#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit


# import unittest

# class TestMaxProfit(unittest.TestCase):
#     def test_emptyList(self):
#         self.assertEqual(Solution().maxProfit([]), 0)

#     def test_onlyOneDay(self):
#         self.assertEqual(Solution().maxProfit([2]), 0)

#     def test_allTheSamePrice(self):
#         self.assertEqual(Solution().maxProfit([2, 2, 2]), 0)

#     def test_positiveExample1(self):
#         self.assertEqual(Solution().maxProfit([7, 1, 5, 3, 6, 4]), 7)

#     def test_positiveExample2(self):
#         self.assertEqual(Solution().maxProfit([8, 4, 6, 2, 10]), 10)

#     def test_positiveExample3(self):
#         self.assertEqual(Solution().maxProfit([8, 4, 6, 2, 1]), 2)

#     def test_positiveExample4(self):
#         self.assertEqual(Solution().maxProfit([1, 2, 3, 4, 5]), 4)

#     def test_negativeExample(self):
#         self.assertEqual(Solution().maxProfit([7, 6, 4, 3, 1]), 0)

# if __name__ == '__main__':
#     unittest.main()
        


