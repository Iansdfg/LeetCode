# class Solution(object):
#     def permuteUnique(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res = []
#         path = []
#         visited = [0] * len(nums)
#         depth = 0
#         self.premu(nums, depth, visited, path, res)
#         return res
#
#     def premu(self, nums, depth, visited, path, res):
#         if depth >= len(nums):
#             res.append(path[:])
#             return
#
#         for i in range(0, len(nums)):
#             if visited[i] == 1:
#                 continue
#             if i > 0 and nums[i] == nums[i-1] and visited[i - 1] == 0:
#                 continue
#             visited[i]=1
#             path.append(nums[i])
#             # print(depth+1, path, visited)
#             self.premu(nums, depth + 1, visited, path, res)
#             path.pop()
#             visited[i] = 0

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        visited = [0]*len(nums)
        nums.sort()
        self.premu(nums, 0, [], res,visited)
        return res

    def premu(self, nums, depth, path, res,visited):
        if len(nums) == len(path):
            print(depth, path, visited)
            res.append(path[:])
            return

        for i in range(0, len(nums)):
            if visited[i] == 1:
                continue
            #
            if i > 0 and nums[i] == nums[i-1] and visited[i - 1] == 0:
                continue

            path.append(nums[i])
            visited[i] = 1
            self.premu(nums, depth + 1, path, res, visited)
            visited[i] = 0
            path.pop()


def execute():
    sol = Solution()
    nums = [3,3,0,3]
    print(sol.permuteUnique(nums))
    # print(nums)

if __name__ == '__main__':
    execute()

