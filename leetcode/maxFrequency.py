#!/usr/bin/env python3
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        res = 1
        for right in range(1, n):
            k -= (nums[right] - nums[right-1]) * (right - left)
            while k < 0:
                k += nums[right] - nums[left]
                left += 1
            res = max(res, right - left + 1)
        return res

test = Solution()

num = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4] 
k = 6
print(f'Return :{test.maxFrequency(num, k)}')
