class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                L = R = mid
                while L>=low and nums[L]==target:
                    L-=1
                while R<=high and nums[R]==target:
                    R+=1
                return [L+1,R-1]
            if nums[low]<=target<nums[mid]:
                high = mid-1
            else:
                low = mid+1
        return [-1,-1]
        # left, right = 0, len(nums)-1
        # if len(nums) == 0:
        #     return [-1, -1]
        # find = None
        # if nums[0] <= target and nums[-1] >= target:
        #     while left<=right:
        #         mid = (left+right)>>1
        #         if nums[mid] == target:
        #             find = mid
        #             break
        #         elif nums[mid] > target:
        #             right = mid-1
        #         elif nums[mid] < target:
        #             left = mid+1
        #     if find == None:
        #         return [-1,-1]
        #     # print(find)
        #     first = last = find
        #     while first-1 >= 0 and nums[first-1] == nums[find]:
        #         first -= 1
        #     while last+1 < len(nums) and nums[last+1] == nums[find]:
        #         last += 1
        #     # print(nums[first+1], nums[last-1], first+1, last-1)
        #     return [first, last]
        # return [-1, -1]




def execute():
    sol = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 6
    nums = [1,1]
    target = 1
    print(sol.searchRange(nums, target))

if __name__ == '__main__':
    execute()



