#!/usr/bin/env python3
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        count = []
        for num in nums:
            smaller_count = sum([freq[key] for key in freq if key < num])
            count.append(smaller_count)
        
        return count

test = Solution()
num = [6,5,4,8]
print(test.smallerNumbersThanCurrent(num))
