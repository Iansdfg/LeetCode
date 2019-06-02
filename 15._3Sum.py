class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # nums.sort()
        # # print(nums)
        # dic={}
        # result = set()
        # length = len(nums)
        # for i in range(length-1):
        #     for j in range(i+1,length):
        #         key = nums[i]+nums[j]
        #         if key in dic.keys():
        #             dic[key].append([i,j])
        #         else:
        #             dic[key] = [[i, j]]
        # # print(dic)
        #
        # for i in range(2,length):
        #     diff = 0-nums[i]
        #     if diff in dic.keys():
        #         # print(dic[diff])
        #         for index in dic[diff]:
        #             if index[1] < i:
        #                 result.add((nums[index[0]],nums[index[1]],nums[i]))
        # print(result)
        # return [list(i) for i in result]

        # nums.sort()
        # result = []
        # for index, value in enumerate(nums):
        #     if index > 0 and nums[index-1] == value:
        #         continue
        #     left, right = index + 1, len(nums) - 1
        #     while left<right:
        #         threeSum = nums[left]+nums[right]+nums[index]
        #         if threeSum < 0:
        #             left += 1
        #         elif threeSum > 0:
        #             right -= 1
        #         else:
        #             result += [[nums[index], nums[left], nums[right]]]
        #             while left < right and nums[right] == nums[right - 1]:
        #                 right -= 1
        #             while left < right and nums[left] == nums[left + 1]:
        #                 left += 1
        #             left += 1
        #             right -= 1
        # return result



        # nums.sort()
        # results = []
        # # print(nums)
        # for index, value in enumerate(nums):
        #     a = value
        #     if index > 0 and nums[index-1] == a:
        #         continue
        #     left = index+1
        #     right = len(nums)-1
        #     while left < right:
        #         # print(left ,right)
        #         if nums[left] + nums[right] + a == 0:
        #             results += [[a, nums[left], nums[right]]]
        #             while left < right and nums[right] == nums[right - 1]:
        #                 right -= 1
        #             right -= 1
        #             while left < right and nums[left] == nums[left + 1]:
        #                 left += 1
        #             left += 1
        #         elif nums[left] + nums[right] + a > 0:
        #             right -= 1
        #         elif nums[left] + nums[right] + a < 0:
        #             left += 1
        # return results

def execute():
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(sol.threeSum(nums))

if __name__ == '__main__':
    execute()

