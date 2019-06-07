class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        if lo == len(nums) - 1 and nums[lo] < target: lo += 1
        if len(nums) == 1 and nums[0] >= target: lo = 0
        return lo
        # insert = 0
        # for index, value in enumerate(nums):
        #     if value == target:
        #         return index
        #     if value < target:
        #         insert += 1
        # return insert



def execute():
    sol = Solution()

    # digits = [1, 3, 5, 6]
    # target = 5
    digits = [1, 3, 5, 6]
    target = 2
    # digits = [1, 3, 5, 6]
    # target = 7
    digits = []
    target = 0

    print(sol.searchInsert(digits,target))

if __name__ == '__main__':
    execute()

