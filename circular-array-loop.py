# 457. Circular Array Loop
# https://leetcode.com/problems/circular-array-loop/

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return False # easy case
        
        def getNext(ix): #next index
            return (ix + nums[ix]) % n
        
        def checkCycle(ix): #check if cycle lenght>1 and all element all positive/negative 
            visited[ix]=True
            if ix == getNext(ix):
                return False
            
            temp = getNext(ix)
            while temp != ix:
                visited[temp]=True
                if nums[temp]*nums[ix]<0:
                    return False
                temp = getNext(temp)
            return True
            
        visited = [False]*n

        for i in range(n):
            if visited[i]: continue
            s = i #slow pointer
            f = i #fast pointer
            while not visited[s]:
                visited[s]=True
                s = getNext(s)
                f = getNext(getNext(f))
                if s == f and checkCycle(s):
                    return True
 
        return False
