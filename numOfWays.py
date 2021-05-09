
#https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/

class Solution:
    def numOfWays(self, n: int) -> int:
      x,y =4,5

      if n==1: return 12
      i=1
      
      while i<n-1:
        x,y=2*x+2*y,2*x+3*y
        i+=1


      return (6*(x+y)) %(10**9+7)

