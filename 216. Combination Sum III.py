class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.dfs(nums, k, n, 0, res, [])
        return res

    def dfs(self, nums, k, n, depth, res, path):
        if k<0 or n<0: return
        if k==0 and n == 0 :
            res.append(path)
            return
        for i in range(depth, len(nums)):
            self.dfs(nums, k-1, n-nums[i], i+1, res, path+[nums[i]])
