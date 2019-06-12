class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        i = 0
        while i < len(nums):
            j = i
            while j < len(nums)-1 and nums[j] == nums[j+1]-1:
                j += 1
            if i == j:
                res.append(nums[i])
            else:
                res.append("%s->%s" % (str(nums[i]),str(nums[j])))
            i = j+1
        return res


def execute():
    sol = Solution()
    s = [0,1,2,4,5,7]
    print(sol.summaryRanges(s))

if __name__ == '__main__':
    execute()
