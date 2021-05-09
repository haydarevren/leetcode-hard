#https://leetcode.com/problems/dice-roll-simulation/

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
      
      #n times 6
      d=[[0]*6 for _ in range(n)]
      #n=1
      d[0]=[1]*6
      
      # pos 2 last=3 i.e. 4 0 index  rollMax[2]
      def dp(pos,last):
        if pos==0: 
          d[pos][last]=1
          return 1 #d[pos] is 1s
        else:
          result=0
          m=rollMax[last]
          j=1
          while j<=m:
            if j>pos:
              result+=1
              break
            for i in range(last-1,last-6,-1): result+=d[pos-j][i]
            j+=1
            
          d[pos][last]=result
          return result  
            
      for pos in range(n):
        for last in range(6):
          dp(pos,last)

      return (sum(d[-1])%(10**9+7))

