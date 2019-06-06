class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summ = 0
        maxx = nums[0]
        for i in range(len(nums)):
            summ += nums[i]
            if summ > maxx:
                maxx = summ
            if summ < 0:
                summ = 0

        return maxx

def execute():
    sol = Solution()
    digits = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(sol.maxSubArray(digits))

if __name__ == '__main__':
    execute()

