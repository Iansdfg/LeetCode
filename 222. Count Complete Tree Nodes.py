# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        Ltree = self.getHeight(root.left)
        Rtree = self.getHeight(root.right)
        if Ltree == Rtree:
            return 2 ** Ltree + self.countNodes(root.right)
        else:
            return  2 ** Rtree + self.countNodes(root.left)
 
        
    def height(self, root):
        if not root:
            return 0
        leftDpth = self.height(root.left)
        rightDpth = self.height(root.right)
        return leftDpth+1 if leftDpth>rightDpth else rightDpth+1
    
    def getHeight(self, node):
        if node is None: return 0
        else: return 1 + self.getHeight(node.left)
        
        
