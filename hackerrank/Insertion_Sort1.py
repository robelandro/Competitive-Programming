#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    tmparr = arr.copy()
    for i in range(n):
        tracker = i
        for j in reversed(range(i)):
            if arr[j] > tmparr[i]:
                arr[j+1] = arr[j]
                tracker = j
                print(arr)
        arr[tracker] = tmparr[i]
    print(arr)
    return arr


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
