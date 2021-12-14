# 253. Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1: return 1
        
        intervals.sort()
        p_que = [intervals[0][1]]

        for s,e in intervals[1:]:
            if s < p_que[0]:
                heapq.heappush(p_que,e)
            else:
                heapq.heapreplace(p_que,e)
                
        return len(p_que)
