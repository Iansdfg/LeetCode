class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        for num in nums:
            if num in dic:
                dic.pop(num)
            else:
                dic[num] = 1
        res = []    
        for key in dic.keys():
            res.append(key)
        return res
        
