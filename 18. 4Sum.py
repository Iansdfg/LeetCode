# class Solution1(object):
#     def fourSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         if not nums or len(nums) <= 3: return []
#         nums.sort()
#         results = []
#         self.nSum(nums, target, 4, [], results)
#         return results
#
#     def nSum(self, nums, target, N, result, results):
#         if N == 2:
#             l, r = 0, len(nums) - 1
#             while l < r:
#                 if nums[l] + nums[r] == target:
#                     results.append(result + [nums[l], nums[r]])
#                     r -= 1
#                     l += 1
#                     while l < r and nums[r] == nums[r + 1]:
#                         r -= 1
#                     while l < r and nums[l] == nums[l - 1]:
#                         l += 1
#                 elif nums[l] + nums[r] > target:
#                     # because array is sorted, apply binary search is faster than r -= 1
#                     r = bisect.bisect_right(nums, target - nums[l], l, r - 1)
#                 else:
#                     # because array is sorted, apply binary search is faster than l += 1
#                     l = bisect.bisect_left(nums, target - nums[r], l + 1, r)
#             return results
#
#         for i in range(0, len(nums) - N + 1):  # careful about range
#             if target < nums[i] * N or target > nums[-1] * N:  # take advantages of sorted list
#                 break
#             if i == 0 or i > 0 and nums[i - 1] != nums[i]:  # recursively reduce N
#                 results = self.nSum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)
#         return results




class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # nums.sort()
        # res, length = [], len(nums)
        # for i in range(length):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     for j in range(i+1,length):
        #         if j>i+1 and nums[j]==nums[j-1]:
        #             continue
        #         left, right = j+1,length-1
        #         while left < right:
        #             if left>j+1 and right<length-1 and nums[left]==nums[left-1] and nums[right]==nums[right+1]:
        #                 left+=1
        #                 right-=1
        #                 continue
        #             val = nums[i]+nums[j]+nums[left]+nums[right]
        #             if val == target:
        #                 res.append([nums[i], nums[j], nums[left], nums[right]])
        #                 right -= 1
        #                 left += 1
        #             elif val > target:
        #                 right -= 1
        #             else:
        #                 left += 1
        # return res
        lens = len(nums)
        dic = {}
        res = set()
        nums.sort()
        for one in range(lens-1):
            for two in range(one+1, lens):
                key = nums[one]+nums[two]

                if key not in dic:
                    dic[key] = [(one, two)]
                else:
                    dic[key].append((one, two))
        # print(dic)dr

        for one in range(lens-1):
            for two in range(one+1, lens):
                pre = target - nums[one] - nums[two]
                if pre in dic:
                    for index in dic[pre]:
                        if index[1] < one:
                            res.add((nums[index[0]], nums[index[1]], nums[one], nums[two]))
        return [list(i) for i in res]

def execute():
    sol = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(sol.fourSum(nums,target))

if __name__ == '__main__':
    execute()

