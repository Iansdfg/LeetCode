class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        print(candidates)
        self.comb(candidates,target,[],0,res)
        return res

    def comb(self, candidates, target, path, depth, res):
        if target == 0:
            res.append(path[:])
            return

        for i in range(depth, len(candidates)):
            if i > depth and candidates[i] == candidates[i-1]:
                continue
            if target < candidates[i]:
                break
            print(path, res)
            self.comb(candidates, target-candidates[i], path+[candidates[i]], i+1, res)



def execute():
    sol = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    candidates = [2,5,2,1,2]
    target = 5
    print(sol.combinationSum2(candidates, target))


if __name__ == '__main__':
    execute()
