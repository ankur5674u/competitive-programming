__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '08-09-2020'

import re

"""
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3411/
"""


class Solution:
    @staticmethod
    def is_palindrome(s: str) -> bool:
        start, end = 0, len(s) - 1
        if not s:
            return True
        while start < end:
            while (start < end) and (not s[start].isalnum()):
                start += 1
            while (start < end) and (not s[end].isalnum()):
                end -= 1
            if (start < end) and s[start].lower() != s[end].lower():
                return False
            start, end = start + 1, end - 1
        return True

    @staticmethod
    def is_palindrome_1(s: str) -> bool:
        if len(s) == 0:
            return True

        pattern = re.compile('[\W_]+')
        s = pattern.sub('', s)
        s = s.lower()
        return s == s[::-1]

    @staticmethod
    def is_palindrome_2(s: str) -> bool:
        if not s:
            return True

        s = ''.join(ch.lower() for ch in s if ch.isalnum())

        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return False

        return True

    @staticmethod
    def is_palindrome_3(s: str) -> bool:
        res = [str(i) for i in s.lower() if i.isalpha() or i.isnumeric()]
        return res == list(reversed(res))
