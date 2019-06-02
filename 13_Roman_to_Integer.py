class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        nums = [dict[c] for c in s]
        cur_value = 0
        pre_value = 0
        print(nums)

        for i in range(len(nums)):
            cur_value += nums[i]
            if pre_value < nums[i]:
                cur_value = cur_value - 2 * pre_value
            pre_value = nums[i]
            print(cur_value,pre_value)
        return cur_value

def execute():
    sol = Solution()
    s = "MCMXCIV"
    print(sol.romanToInt(s))

if __name__ == '__main__':
    execute()

