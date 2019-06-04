#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#

class Solution():
    def countBinarySubstrings(self, s: str) -> int:
        countList = list(map(len, s.replace("01", "0 1").replace("10", "1 0").split()))
        return sum(min(first, second) for first, second in zip(countList, countList[1:]))

# import unittest

# class TestCountBinarySubstrings(unittest.TestCase):
#     def testExample1(self):
#         self.assertEqual(Solution().countBinarySubstrings("00110011"), 6)

#     def testExample2(self):
#         self.assertEqual(Solution().countBinarySubstrings("10101"), 4)

#     def testExample3(self):
#         self.assertEqual(Solution().countBinarySubstrings("11100101100"), 7)

#     def testAllTheSame(self):
#         self.assertEqual(Solution().countBinarySubstrings("000000"), 0)

#     def testEmpty(self):
#         self.assertEqual(Solution().countBinarySubstrings(""), 0)

# if __name__ == '__main__':
#     unittest.main()
