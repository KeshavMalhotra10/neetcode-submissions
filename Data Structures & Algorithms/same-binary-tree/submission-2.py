# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #basecase:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val == q.val:
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            return left and right
        else:
            return False

        #basecase should be if p or q is none
        # if p == None and q == None:
        #     return True
        # elif p == None or q == None:
        #     return False
        # else:
        #     return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
        
        