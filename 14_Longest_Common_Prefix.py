class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        add = 1
        result = ''
        if len(strs) == 0:
            return ''
        while i < len(strs[0]):
            tar = strs[0][i]
            for ele in strs:
                if i > len(ele)-1:
                    add *= 0
                    break
                if ele[i] == tar:
                    add *= 1
                else:
                    add *= 0
            if add == 1:
                result += tar
            else:
                break
            i += 1
        return result


def execute():
    sol = Solution()
    s = ["aa","a"]
    print(sol.longestCommonPrefix(s))

if __name__ == '__main__':
    execute()

