class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        tar = abs(x)
        result = 0
        length = len(str(abs(x)))
        while tar >= 10:
            result += (tar%10)*10**(length-1)
            tar = int(tar/10)
            length = length-1
        if tar + result > 2**31-1 or tar + result<-(2**31):
            return 0
        if x > 0:
            return tar + result
        else:
            return -(tar + result)

def execute():
    sol = Solution()
    x = 1534236469
    print(sol.reverse(x))


if __name__ == '__main__':
    execute()

