class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        constraints for a valid tree:
        1. No cycles: no loops or closed paths connecting nodes to itself
        2. Connected graph: by following edges, you should be able to get to any 2 different nodes

        Solution 1:
        1. DFS Solution: start at top node and check for conditions stated above, check for cycles by seeing if node in visited set

        '''
        #check empty case
        if not n:
            return True

        visited = set()
        #print(edges[0][0])
        nodeNeighbour = {i:[] for i in range(n)} #empty lists for index

        #map neighbours to nodes:
        for node, nei in edges:
            nodeNeighbour[node].append(nei)
            nodeNeighbour[nei].append(node)
        
        #print(nodeNeighbour)
        
        def dfs(node, prev):
            #check 1. is this node visited?
            if node in visited:
                return False
            #else perform dfs on neighbours
            visited.add(node)
            for nei in nodeNeighbour[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0,-1) and n == len(visited)
        

        
            
        
