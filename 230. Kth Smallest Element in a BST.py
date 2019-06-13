# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        self.inorder(root, res)
        # print(res)
        return res[k-1]
        
        
    def inorder(self,root, res):
        if root:
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)
        
    
        
