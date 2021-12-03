# 174. Dungeon Game
# https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        m = len(dungeon)
        n = len(dungeon[0])
        
        healthreq = [[10001 for j in range(n+1)] for i in range(m+1)]
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    healthreq[i][j]= max(1,1-dungeon[i][j])
                else:
                    bestroute=min(healthreq[i+1][j]- dungeon[i][j], healthreq[i][j+1]- dungeon[i][j]) #up vs left
                    healthreq[i][j]= max(1, bestroute ) 

        return healthreq[0][0]
    
