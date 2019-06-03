class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []






def execute():
    sol = Solution()

    digits = "{[]}"

    print(sol.isValid(digits))

if __name__ == '__main__':
    execute()

