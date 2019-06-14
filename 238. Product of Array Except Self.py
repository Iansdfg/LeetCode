class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0]*len(nums)
        tmp = 1
        for i in range(len(nums)):
            res[i] = tmp
            tmp *= nums[i]
        tmp = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= tmp
            tmp *= nums[i]
        return res




def execute():
    sol = Solution()
    nums = [1, 2, 3, 4]
    print(sol.productExceptSelf(nums))

if __name__ == '__main__':
    execute()

