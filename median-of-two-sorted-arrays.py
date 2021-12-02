# https://leetcode.com/problems/median-of-two-sorted-arrays/

import heapq

class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def medianSortedArray(nums):
            if len(nums)%2: return nums[len(nums)//2]
            else: return  0.5* (nums[len(nums)//2] + nums[len(nums)//2-1])
        
        if not nums1: return medianSortedArray(nums2)
        if not nums2: return medianSortedArray(nums1)
        small = []
        large = []
        small.extend([-i for i in nums1[:len(nums1)//2]])
        small.extend([-i for i in nums2[:len(nums2)//2]])
        large.extend(nums1[len(nums1)//2:])
        large.extend(nums2[len(nums2)//2:])
        heapq.heapify(small)
        heapq.heapify(large)

        if len(large)>len(small)+1:
            heapq.heappush(small,-heapq.heappop(large)) 
        while large[0]<-small[0]:
            heapq.heappush(large,-heapq.heappop(small))
            heapq.heappush(small,-heapq.heappop(large))
                   

        if len(large)>len(small): return large[0]
        else: return 0.5*(large[0] - small[0])
