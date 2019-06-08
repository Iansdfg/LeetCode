class Solution(object):
    # def minSubArrayLen(self, s, nums):
    #     """
    #     :type s: int
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     """
    #     O(n)
    #     """
    #     N = len(nums)
    #     l, r = 0, 0
    #     csum = 0
    #     res = len(nums)+1
    #     while r < N:
    #         csum += nums[r]
    #         while csum >= s:
    #             res = min(res, r - l + 1)
    #             csum -= nums[l]
    #             l += 1
    #         r += 1
    #     return res if res != len(nums)+1 else 0
    """
    O(nlog(n))
    """
    def minSubArrayLen(self, s, nums):
        lens = len(nums)
        sums = [0]*(lens+1)
        res = lens + 1
        for i in range(1,len(sums)):
            sums[i] = sums[i - 1] + nums[i - 1]
        for i in range(len(sums)):
            right = self.searchRight(i + 1, lens, sums[i] + s, sums)
            if right == lens + 1: break
            if res > right - i:
                res = right - i

        return 0 if res == lens + 1 else res



    def searchRight(self, left, right, s, sums):
        while left <= right:
            mid = (left + right) // 2
            if sums[mid] >= s:
                right = mid - 1
            else:
                left = mid + 1
        return left


def execute():
    s, nums = 7, [2, 3, 1, 2, 4, 3]
    # s, nums = 15,[1, 2, 3, 4, 5]
    sol = Solution()
    print(sol.minSubArrayLen(s, nums))

if __name__ == '__main__':
    execute()

