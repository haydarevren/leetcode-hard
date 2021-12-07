# 75. Sort Colors
# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        p0=p1=p2=0 #pointers 
        for i in range(len(nums)): # sliding window
            if nums[i]==0:
                if p0<p2: #otherwise no need for swap (teher are only 0's)
                    if p0 < p1 and p1<p2: #if there are some 1's and 2's
                        nums[p0], nums[p1], nums[i] = nums[i], nums[p0], nums[p1]
                    else: #if there are either some 1's or 2's
                        nums[p0], nums[i]= nums[i], nums[p0]
                p0+=1
                p1+=1
                p2+=1

            elif nums[i]==1:
                if p1<p2: #otherwise no need for swap
                    nums[p1], nums[i] = nums[i], nums[p1]
                p1+=1
                p2+=1
            
            else:
                p2+=1
