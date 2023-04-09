#!/usr/bin/python3
from typing import List

class Solution:
        def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            li = [(x[0] ** 2 + x[1] ** 2, x) for x in points]
            li.sort(key=lambda x: x[0])
            return [x[1] for x in li[:k]]
