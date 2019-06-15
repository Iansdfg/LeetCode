class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        res = []
        for i in range(len(input)):
            if input[i] == "+" or input[i] == "-" or input[i] == "*":
                lefts = self.diffWaysToCompute(input[:i])
                rights = self.diffWaysToCompute(input[i+1:])
                for left in lefts:
                    for right in rights:
                        if input[i] == "+":
                            res.append(left + right)
                        elif input[i] == "-":
                            res.append(left - right)
                        elif input[i] == "*":
                            res.append(left * right)
        if not res:
            res.append(int(input))
        return res
