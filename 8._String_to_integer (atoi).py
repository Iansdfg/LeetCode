class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        result = 0
        sign = 1
        str = str.strip()
        if len(str) == 0:
            return 0
        start = 0
        end = len(str)
        if str[0] == '+':
            sign = 1
            start = 1
        elif str[0] == '-':
            sign = -1
            start = 1
        for i in range(start, end):
            if str[i].isdigit():
                result = result * 10 + int(str[i])
            else:
                break
        result = result * sign
        result = max(min(result, 2 ** 31 - 1), -2 ** 31)
        return result





def execute():
    sol = Solution()
    s = "words and 987"

    print(sol.myAtoi(s))


if __name__ == '__main__':
    execute()

