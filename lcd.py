#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 hkr <hkr@hkr-Laptop>
#
# Distributed under terms of the MIT license.

"""

"""
from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1, text2):
        
        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0

            option1 = memo_solve(p1+1, p2)

            option2 = 0
            first_occurence = text2.find(text1[p1], p2)
            if first_occurence != -1:
                option2 = 1 + memo_solve(p1+1, first_occurence+1)
            
            return max(option1, option2)
        return memo_solve(0,0)


s = Solution()
text1 = input('Enter first: ')
text2 = input('Enter second: ')
print(s.longestCommonSubsequence(text1, text2))
