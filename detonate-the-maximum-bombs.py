# 2101. Detonate the Maximum Bombs
# https://leetcode.com/problems/detonate-the-maximum-bombs/

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        if len(bombs) <=1: return len(bombs)
        
        def isDetonate(i,j):
            dist = ( (bombs[i][0] - bombs[j][0])**2 +  (bombs[i][1] - bombs[j][1])**2 )**0.5
            return bombs[i][2] >= dist, bombs[j][2] >= dist 
            
        graph = collections.defaultdict(list)
        for i,j in itertools.combinations(range(len(bombs)),2):
            d =  isDetonate(i,j)   
            if d[0]: graph[i].append(j)
            if d[1]: graph[j].append(i)
            
        if len(graph) <= 1: return len(graph)+1
        
        def dfs(start):
            cur_det = 0
            seen = set()
            que = [start]
            while que:
                i = que.pop()
                if i not in seen:
                    cur_det+=1
                    seen.add(i)
                    que.extend(graph[i])
            return cur_det
        
        nodelist = list(graph.keys())
        
        
        return max(dfs(i) for i in nodelist)       
