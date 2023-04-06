#!/usr/bin/env python3
#User function Template for python3

class Solution: 
    def select(self, arr, i):
        current_min = i
        for x in range(i+1, len(arr)):
            if arr[x] < arr[current_min]:
                current_min = x
        return current_min
    
    def selectionSort(self, arr,n):
        for x in range(n):
            change_index = self.select(arr, x)
            arr[x] , arr[change_index] = arr[change_index] , arr[x]
        
        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
