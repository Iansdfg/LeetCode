class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 and not num2: return '0'
        if num1 == '0' or num2 == '0': return '0'
        digits = [0] * (len(num1) + len(num2))
        m, n = len(num1), len(num2)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                product = int(num1[i]) * int(num2[j])
                p1, p2 = j + i, j + i + 1
                sum = product + digits[p2]
                digits[p1] += sum // 10
                digits[p2] = sum % 10
                print(digits)
        res = ''
        for digit in digits:
            if not(digit == 0 and len(res) == 0):
                res += str(digit)
        return res


        # if not num1 and not num2: return '0'
        # if num1 == '0' or num2 == '0': return '0'
        # num1, num2 = num1[::-1], num2[::-1]
        # m, n = len(num1), len(num2)
        # digit = [0]*(len(num1)+len(num2))
        # for i in range(m):
        #     for j in range(n):
        #         p1, p2 = j + i, j + i + 1
        #         product = int(num1[i])*int(num2[j])
        #         units = product % 10
        #         carry = product // 10
        #         digit[p1] += units
        #         if units>=10:
        #             carry+=units//10
        #             units = units % 10
        #         digit[p2] += carry
        # print(digit)
        # carry = 0
        # res = ''
        # for i in range(len(digit)):
        #     digit[i] += carry
        #     carry = 0
        #     if digit[i] >= 10:
        #         carry = digit[i] // 10
        #         digit[i] = digit[i] % 10
        #     res += str(digit[i])
        # # print(res)
        # res = res[::-1]
        # while res[0] == '0':
        #     res = res[1:]
        # return res


def execute():
    sol = Solution()
    num1 = "123"
    num2 = "456"
    print(sol.multiply(num1, num2))


if __name__ == '__main__':
    execute()
