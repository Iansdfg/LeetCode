class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        depth = 0
        self.getCom(candidates, target,depth, res, [])
        return res

    def getCom(self, candidates, target, depth, res, path):
        if sum(path) > target:
            return
        if sum(path) == target:
            res += [path]
        for i in range(depth, len(candidates)):
            self.getCom(candidates, target, i, res, path + [candidates[i]])



def execute():
    sol = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    # candidates = [2, 3, 5]
    # target = 8
    print(sol.combinationSum(candidates, target))


if __name__ == '__main__':
    execute()
