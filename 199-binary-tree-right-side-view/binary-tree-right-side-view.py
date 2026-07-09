# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
    
        q = deque([root])
        res = []
        
        while q:
            length = len(q)
            for i in range(length):
                popped = q.popleft()
           
                if i == length - 1:
                    res.append(popped.val)
                
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
        
        return res
            
