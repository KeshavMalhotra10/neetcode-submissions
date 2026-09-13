# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #case 1. either tree is empty
        if not p and q:
            return False
        if not q and p:
            return False
        if not q and not p:
            return True
        
        #case 2. the two nodes values are not equal
        if p.val != q.val:
            return False
        
        #case 3. if left or right values are empty
        
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        
        