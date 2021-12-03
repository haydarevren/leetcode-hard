# 815. Bus Routes
# https://leetcode.com/problems/bus-routes/

from collections import defaultdict
import itertools
from collections import deque 

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        #easy case
        if source==target: return 0
        
        #create adjacency graph and grph for routes 
        def createGraph(routes):
            graph_stop=defaultdict(set)
            for i, stops in enumerate(routes):
                # graph_bus[i]=set(stops)
                for j in stops:
                    graph_stop[j].add(i)
                    
            graph_bus=defaultdict(set)
            for stop in graph_stop.keys():
                for i,j in itertools.combinations(graph_stop[stop],2):
                    graph_bus[i].add(j)
                    graph_bus[j].add(i)

            return graph_bus,graph_stop
        
        graph_bus,graph_stop = createGraph(routes)
        
        s_buses = graph_stop[source]
        t_buses = graph_stop[target]
        
        #easy case
        if not s_buses or not t_buses: return -1
        
        #find the shortest path between set s and set t using BFS
        def shortestpath(graph, s, t):
            
            dist = 1
            # If the desired node is reached
            if s.intersection(t): return dist
            
            # Queue for traversing the
            # graph in the BFS
            queue = deque()
            explored = s.copy()
            
            dist+=1
            for v in s:
                for neighbor in graph[v]:
                    if neighbor not in explored:
                        if neighbor in t: return dist
                        queue.append(neighbor)
                        explored.add(neighbor)
                
                
            while queue:
                dist+=1
                v = queue.popleft()
                for neighbor in graph[v]:
                    if neighbor not in explored:
                        if neighbor in t: return dist
                        queue.append(neighbor)
                        explored.add(neighbor)

            return -1

        return shortestpath(graph_bus,s_buses,t_buses)
