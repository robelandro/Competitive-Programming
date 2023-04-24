#!/usr/bin/env python3

from typing import List
import collections

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum([v*(v-1)//2 for v in collections.Counter(nums).values()])

test = Solution()

nums = [1,2,3]

print(test.numIdenticalPairs(nums))
