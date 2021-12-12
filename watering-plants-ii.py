# 2105. Watering Plants II
# https://leetcode.com/problems/watering-plants-ii/

class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        if len(plants)<=2: return 0
        
        res =0 
        l =0
        r = len(plants)-1
        a =capacityA
        b =capacityB
        while r-l>0:
            if plants[l]<=a:
                a -= plants[l] 
            else:
                a =capacityA - plants[l]
                res+=1 
            l+=1
            
            if plants[r]<=b:
                b -= plants[r]  
            else:
                b =capacityB - plants[r]
                res+=1
            r-=1

        if r-l==0 and max(a,b)<plants[l]: res +=1        
            
        return res
