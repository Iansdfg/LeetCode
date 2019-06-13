class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = n = cut_m = cut_n = 0
        for num in nums:
            if num == m:
                cut_m += 1
            elif num == n:
                cut_n += 1
            elif cut_m == 0:
                m = num
                cut_m = 1
            elif cut_n == 0:
                n = num
                cut_n = 1
            else:
                cut_m -= 1
                cut_n -= 1
        # print(m, n,  cut_m, cut_n)
        cut_m = cut_n = 0
        for num in nums:
            if num == m:
                cut_m += 1
            elif num == n:
                cut_n += 1
        # print(m, n, cut_m, cut_n)
        res = []
        if cut_m > len(nums) // 3:
            res.append(m)
        if cut_n > len(nums) // 3:
            res.append(n)
        return res







def execute():
    sol = Solution()
    nums = [3, 2, 3]
    # nums = [1,1,1,3,3,2,2,2]
    print(sol.majorityElement(nums))

if __name__ == '__main__':
    execute()

