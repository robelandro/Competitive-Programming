#!/usr/bin/env python3
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = [0] * len(nums)
        result[::2], result[1::2] = nums[len(nums)//2:], nums[:len(nums)//2]
        return result


test = Solution()

# nums = [10,8,7,11,6,1]
nums = [1,2,3]
print(test.rearrangeArray(nums))
