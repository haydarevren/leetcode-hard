# 435. Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) ==1 : return 0
        intervals = sorted(intervals)
        
        res = 0
        i, j= 0, 1
        while i<len(intervals) and j<len(intervals):
            s0,e0 =intervals[i]
            s1,e1 =intervals[j]
            # 3 cases
            # s0 <= s1 < e0 <=  e1 => res+=1 j+=1
            # s0 < e0 <= s1 < e1 => i->j  , j->i+1
            # s0 <= s1 <  e1 < e0 => res+=1 i->j, j->i+1
            if e0<=s1: i=j;j=i+1
            else:
                res+=1
                if e1<e0: i=j; j=i+1
                else: j+=1
        return res
