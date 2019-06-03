class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        diff = abs(target-(nums[0]+nums[1]+nums[2]))
        mini = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            left = i + 1
            right = len(nums)-1
            if i>1 and nums[i] == nums[i-1]:
                continue
            while left<right:
                print(diff, mini)
                threeSum = nums[i]+nums[left]+nums[right]
                if threeSum>target:
                    if abs(target-threeSum)<diff:
                        diff = abs(target-threeSum)
                        mini = threeSum
                    right -= 1
                elif threeSum<target:
                    if abs(target-threeSum)<diff:
                        diff = abs(target-threeSum)
                        mini = threeSum
                    left += 1
                else:
                    return threeSum
        return mini
        # nums.sort()
        # # print(nums)
        # minDis = abs((nums[0]+nums[1]+nums[2])-target)
        # result = 0
        # for index, value in enumerate(nums):
        #     val = value
        #     if index > 0 and nums[index-1] == val:
        #         continue
        #     left = index+1
        #     right = len(nums)-1
        #     while left < right:
        #         total = val + nums[left] + nums[right]
        #         # print(index, val, nums[left], nums[right] , total)
        #         dis = abs(total - target)
        #         if minDis >= dis:
        #             # print(index, "here")
        #             minDis = dis
        #             result = total
        #         if total < target:
        #             left += 1
        #         elif total >= target:
        #             right -= 1
        #         # print('index', index, 'left', left, 'right', right, 'total', total, 'miniDis',minDis,'dis', dis, 'result',result)
        # return result

def execute():
    sol = Solution()
    nums = [1,1,1,0]
    target = -100
    # nums = [-1, 2, 1, -4]
    # target = 1
    # nums = [0, 2, 1, -3]
    # target = 1
    # nums = [-1, 2, 1, -4]
    # target = 1
    # nums = [1, 1, -1, -1, 3]
    # target = -1
    print(sol.threeSumClosest(nums, target))

if __name__ == '__main__':
    execute()

