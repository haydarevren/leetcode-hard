# 581. Shortest Unsorted Continuous Subarray
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        
        l=r=0
        #find the largest index not in place
        old=-10_001
        for i,num in enumerate(nums):
            if old<=num:
                old=num
            else:
                r = i

        if r==0: #if everything is already sorted
             return 0
            
        #find the smallest index not in place
        old=10_001
        for i,num in enumerate(nums[::-1]):
            if old>=num:
                old=num
            else:
                l = len(nums)-1-i

        return r-l+1
