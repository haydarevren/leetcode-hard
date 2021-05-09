#https://leetcode.com/problems/number-of-operations-to-make-network-connected/

#Soln 1
def makeConnected(comp_nodes, comp_from, comp_to):

    if len(comp_from)<comp_nodes-1:
        return -1
    G=dict([i,set()] for i in range(1,comp_nodes+1))

    for i in range(len(comp_from)):
        G[comp_from[i]].add(comp_to[i])
        G[comp_to[i]].add(comp_from[i])

    def DFS(start,visited):
        for e in G[start]:
            if e not in visited:
                visited.add(e)
                DFS(e,visited)

    num_parts=0
    not_visited_comps=set(i for i in range(1,comp_nodes+1))
    while not_visited_comps:
        initial_node=not_visited_comps.pop()
        con_comps={initial_node}
        num_parts+=1
        DFS(initial_node,con_comps)
        not_visited_comps-=con_comps

    return num_parts-1

#Soln 2
def makeConnected(comp_nodes, comp_from, comp_to):
    if len(comp_from)<comp_nodes-1:
        return -1

    G = [set() for i in range(comp_nodes)]
    for i, j in connections:
        G[i-1].add(j-1)
        G[j-1].add(i-1)

    seen = [0] * comp_nodes

    def dfs(i):
        if seen[i]: return 0
        seen[i] = 1
        for j in G[i]: dfs(j)
        return 1

    return sum(dfs(i) for i in range(comp_nodes)) - 1

print(makeConnected(4,[1,1,2],[2,3,3]))