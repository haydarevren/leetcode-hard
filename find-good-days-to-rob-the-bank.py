# 2100. Find Good Days to Rob the Bank
# https://leetcode.com/problems/find-good-days-to-rob-the-bank/

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        #easy cases
        if time == 0: return [i for i in range(len(security))]
        if 2*time + 1 > len(security): return [] 
        
        res=set()
        
        p=0
        i=1
        while i < (len(security)-time):
            if security[i]>security[i-1]:
                p=i
                
            if i-p>= time : res.add(i)
            i+=1
                
        p=len(security) - 1
        i=len(security) - 2
        while i >time-1:
            if security[i]>security[i+1]:
                p=i
                
            if p-i< time and i in res: res.remove(i)

            i-=1
           
        return sorted(list(res))
            
        
