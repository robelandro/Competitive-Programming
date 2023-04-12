#!/usr/bin/env python3

from typing import List

import heapq

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        k_largest = []
        for num in nums:
            num_int = int(num)
            if len(k_largest) < k:
                heapq.heappush(k_largest, num_int)
            else:
                heapq.heappushpop(k_largest, num_int)
        return str(k_largest[0])
        

test = Solution()

nums = ["2","21","12","1"]
k = 3
print(test.kthLargestNumber(nums, k))
