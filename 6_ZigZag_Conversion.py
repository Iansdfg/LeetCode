class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = ''
        length = len(s)
        n = numRows
        cycle = 2*n-2
        if n == 1:
            return s
        # i is the number of line
        # x is number of cycle
        i = 0
        x = 0
        while len(result) < length:
            if cycle * x + i > length - 1:
                i += 1
                x = 0
            zig = cycle * x + i
            zag = cycle * (x+1) - i
            if i == 0 or i == n-1:
                result += s[zig]
            else:
                if zag > length - 1:
                    result += s[zig]
                else:
                    result += s[zig]+s[zag]
            x += 1
            print(result)
        return result


def execute():
    sol = Solution()
    s = "PAYPALISHIRING"
    numRows = 4
    print(sol.convert(s, numRows))


if __name__ == '__main__':
    execute()

