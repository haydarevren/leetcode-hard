# 986. Interval List Intersections
# https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList: return []
        
        def getIntersection(list1, list2):
            if max(list1[0],list2[0]) <= min(list1[1],list2[1]):
                return [max(list1[0],list2[0]), min(list1[1],list2[1])]
            else:
                return None
            
        p1 = p2 = 0
        result=[]
        while p1<len(firstList) and p2<len(secondList):
            result.append(getIntersection(firstList[p1], secondList[p2]))
            if firstList[p1][1] > secondList[p2][1]:
                p2+=1
            elif secondList[p2][1] > firstList[p1][1]:
                p1+=1
            else:
                p1+=1
                p2+=1
                
        return [interval for interval in result if interval is not None]
