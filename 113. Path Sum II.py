# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root: return 0
        return self.dfs(root, sum)+self.pathSum(root.left, sum)+self.pathSum(root.right, sum)
    
    def dfs(self, root, sum):
        if not root: return
        res = 0
        sum -= root.val
        if sum==0:
            res +=1
        if root.left:
            res += self.dfs(root.left, sum)
        if root.right:
            res += self.dfs(root.right, sum)
        return res
        
    
