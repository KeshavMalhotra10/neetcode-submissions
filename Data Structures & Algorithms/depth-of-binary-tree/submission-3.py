# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)'''

        #alternate solution
        '''if not root:
            return 0 
        q = deque([root])
        level = 0 
        
        while q:
            for i in range (len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level +=1
        return level'''

        #the last solution
        st = [(root, 1)] #initialize stack with root value
        maxDepth = 0

        if not root:
            return 0

        while st:
            myNode, depth = st.pop()

            maxDepth = max(maxDepth, depth)

            if myNode.left:
                st.append((myNode.left, depth + 1))
                
            if myNode.right:
                st.append((myNode.right, depth + 1))
        return maxDepth
            
        
        



        