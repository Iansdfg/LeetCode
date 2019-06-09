class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        lens = len(nums)
        return max(self.rob_range(nums[:lens-1]),self.rob_range(nums[1:]))

    def rob_range(self, nums):
        if not nums: return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        lens = len(nums)
        dp = [0] * lens
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, lens):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]


def execute():
    sol = Solution()
    nums = [1,2,3,1]
    print(sol.rob(nums))

if __name__ == '__main__':
    execute()

