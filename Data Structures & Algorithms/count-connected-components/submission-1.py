class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        Solutions:
        1. Analyze all nodes through dfs, and update a counter every time a cycle appears, return the counter, Time O(n), Space O(n)
        2. Analyze where the breaks are(doesnt work)
        '''
        #edge cases if n = 0
        if not n:
            return 0

        nodeToNei = {i:[] for i in range(n)}
        for node, nei in edges:
            nodeToNei[node].append(nei) 
            nodeToNei[nei].append(node)
        print(nodeToNei)
        
        visited = set()
        numComponents = 0

        def dfs(node):
            #check 1. is node visited
            if node in visited:
                return
            #check 2. what if no neighbours
            if nodeToNei[node] == []:
                return
            visited.add(node)
            #Run dfs on all the neighbours
            for nei in nodeToNei[node]:
                if nei not in visited:
                    dfs(nei)
        
        for node in nodeToNei:
            if node not in visited:
                numComponents+=1
                dfs(node)

        return numComponents
        
            


        



