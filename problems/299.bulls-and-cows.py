#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#
# https://leetcode.com/problems/bulls-and-cows/description/
#
# algorithms
# Medium (38.88%)
# Total Accepted:    91.9K
# Total Submissions: 236.3K
# Testcase Example:  '"1807"\n"7810"'
#
# You are playing the following Bulls and Cows game with your friend: You write
# down a number and ask your friend to guess what the number is. Each time your
# friend makes a guess, you provide a hint that indicates how many digits in
# said guess match your secret number exactly in both digit and position
# (called "bulls") and how many digits match the secret number but locate in
# the wrong position (called "cows"). Your friend will use successive guesses
# and hints to eventually derive the secret number.
#
# Write a function to return a hint according to the secret number and friend's
# guess, use A to indicate the bulls and B to indicate the cows.
#
# Please note that both secret number and friend's guess may contain duplicate
# digits.
#
# Example 1:
#
#
# Input: secret = "1807", guess = "7810"
#
# Output: "1A3B"
#
# Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
#
# Example 2:
#
#
# Input: secret = "1123", guess = "0111"
#
# Output: "1A1B"
#
# Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a
# cow.
#
# Note: You may assume that the secret number and your friend's guess only
# contain digits, and their lengths are always equal.
#


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        counter = [0 for i in range(10)]
        for s, g in zip(map(int, secret), map(int, guess)):
            if s == g:
                bulls += 1
                continue
            cows += sum([counter[s] < 0, counter[g] > 0])
            counter[s] += 1
            counter[g] -= 1

        return '{bulls}A{cows}B'.format(bulls=bulls, cows=cows)


"""
# Another approach:
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        counterS = [0 for i in range(10)]
        counterG = [0 for i in range(10)]

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                counterS[int(s)] += 1
                counterG[int(g)] += 1

        cows = sum([min(counterS[i], counterG[i]) for i in range(10)])

        return '{bulls}A{cows}B'.format(bulls=bulls, cows=cows)
"""

"""
import unittest


class TestGetHint(unittest.TestCase):
    def test_allMiss(self):
        self.assertEqual(Solution().getHint('123', '312'), '0A3B')

    def test_allDifferent(self):
        self.assertEqual(Solution().getHint('12345', '67890'), '0A0B')

    def test_allCorrect(self):
        self.assertEqual(Solution().getHint('123456', '123456'), '6A0B')

    def test_partialCorrect(self):
        self.assertEqual(Solution().getHint('11223344', '11224433'), '4A4B')

    def test_duplicatedMatch1(self):
        self.assertEqual(Solution().getHint('1123', '0111'), '1A1B')

    def test_duplicatedMatch2(self):
        self.assertEqual(Solution().getHint('1111100000', '9911111088'), '4A2B')

if __name__ == '__main__':
    unittest.main()
"""
