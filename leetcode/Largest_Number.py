#!/usr/bin/env python3
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(key=lambda x: x * 10, reverse=True)
        return str(int(''.join(nums)))

test = Solution()
nums = [0,0]
# nums = [12, 10, 29, 20, 2, 200, 300, 301, 30, 32, 90]

print(test.largestNumber(nums)) # 90 32 30 301 300 29 2 20 200 12 10
