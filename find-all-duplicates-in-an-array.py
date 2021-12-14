# 442. Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for num in nums: nums[abs(num)-1] *=-1       
        return set(abs(num) for num in nums if nums[abs(num)-1]>0)
