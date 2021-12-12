# 2106. Maximum Fruits Harvested After at Most K Steps
# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:

        def checkPos(leftPos,rightPos):
            if leftPos>=startPos: 
                return rightPos<=startPos+k
            else:
                leftmove = startPos-leftPos
                rightmove = rightPos-startPos
                return 2*leftmove+rightmove<=k or 2*rightmove+leftmove<=k
        
        #initialize the sliding window
        lx = rx = None
        for i,fr in enumerate(fruits):
            if fr[0]>startPos+k: break
            if fr[0]>=startPos-k:
                lx = rx = i
                lPos = rPos = fr[0]
                break
        
        if lx is None: return 0
        
        out = 0 
        
        cur_total = fruits[lx][1]
        while checkPos(lPos,rPos+1):
            rPos+=1
            if rx+1<len(fruits) and fruits[rx+1][0]<= rPos:
                rx+=1
                cur_total += fruits[rx][1]
                
        out = max(out, cur_total)
        
        while lPos<= startPos:
            lPos+=1
            if lx<len(fruits) and fruits[lx][0]< lPos:
                cur_total -= fruits[lx][1]
                lx+=1
            while checkPos(lPos,rPos+1):
                rPos+=1
                if rx+1<len(fruits) and fruits[rx+1][0]<= rPos:
                    rx+=1
                    cur_total += fruits[rx][1]
            out = max(out, cur_total)
            
        return out
