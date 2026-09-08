"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

'''
Solution 1: Go through each node using DFS and add the neighbours to a result list Time: o(n), Space O(n)

'''

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #hashmap to track clones

        oldToNew = {}

        def dfs(node):
            #first check to see if node has already been added
            if node in oldToNew:
                return oldToNew[node] #return the clone copy
            
            #lets make our copy now
            copy = Node(node.val)
            oldToNew[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node) if node else None

        