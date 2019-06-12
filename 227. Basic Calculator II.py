class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        pre_op = '+'
        num = 0
        for i, each in enumerate(s):
            # print(i,each)
            if each.isdigit():
                num = num*10 + int(each)
            if i == len(s) - 1 or each in '+-*/':
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop()*num)
                elif pre_op == '/':
                    top = stack.pop()
                    if top < 0:
                        stack.append((-top)//num*-1)
                    else:
                        stack.append(top//num)
                pre_op = each
                num = 0
        return sum(stack)


def execute():
    sol = Solution()
    s = "3+2*2"
    print(sol.calculate(s))

if __name__ == '__main__':
    execute()
