class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        tar = x
        if x < 0:
            return False
        result = 0
        while x > 0:
            result = result*10 + x % 10
            x = int(x / 10)
        if result == tar:
            return True
        
def execute():
    sol = Solution()
    s = 121
    print(sol.isPalindrome(s))

if __name__ == '__main__':
    execute()
