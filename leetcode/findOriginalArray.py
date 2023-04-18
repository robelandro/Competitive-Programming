#!/usr/bin/env python3

import collections
from typing import List

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        freq = collections.Counter(changed)
        original = []
        for num in sorted(changed):
            if freq[num] == 0:
                continue
            if 2 * num in freq and freq[2 * num] > 0:
                original.append(num)
                freq[num] -= 1
                freq[2 * num] -= 1
            elif num % 2 == 0 and num // 2 in freq and freq[num // 2] > 0:
                original.append(num // 2)
                freq[num] -= 1
                freq[num // 2] -= 1
            else:
                return []
        return original
 
test  = Solution()
changed = [1,3,4,2,6,8]
print(test.findOriginalArray(changed)) # 1 3 4 8
