class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        while len(s)>1:
            res = 0
            for i in range(len(s)):
                res+=int(s[i])
            s = str(res)
        return int(s)
                
        if num == 0:
            return 0
        else:
            return 1 + (num - 1) % 9
