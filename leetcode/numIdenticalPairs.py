#!/usr/bin/env python3

from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for n in range(len(nums)):
            for m in range(n+1, len(nums)):
                if (nums[n] == nums[m]):
                    count+=1
        return count

test = Solution()

nums = [1,2,3]

print(test.numIdenticalPairs(nums))
