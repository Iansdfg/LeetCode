 class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index, value in enumerate(nums):
            if value in dic.keys():
                return [dic[value],index]
            else:
                dic[target-value] = index


        # dic = {}
        # for index, item in enumerate(nums):
        #     if item in dic.keys():
        #         return [dic[item], index]
        #     else:
        #         dic[target-item] = index


def execute():
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    nums=[3, 2, 4]
    target=6
    print(sol.twoSum(nums,target))

if __name__ == '__main__':
    execute()

