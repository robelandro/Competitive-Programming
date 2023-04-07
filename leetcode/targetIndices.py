#!/usr/bin/env python3
from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        index = []
        for j in range(len(nums)):
            if nums[j] == target:
                index.append(j)
        return index
