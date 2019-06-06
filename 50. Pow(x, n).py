class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)

    # Iteration
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        while n:
            if n % 2:
                ans *= x
            n = n//2
            x *= x
        return ans


def execute():
    sol = Solution()
    # x, n = 2.00000, -5
    # # # x, n = 2.00000, -2
    x, n = 2, 4
    print(sol.myPow(x, n))


if __name__ == '__main__':
    execute()
