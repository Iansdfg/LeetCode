class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for str in strs:
            sortedstr = "".join(sorted(str))
            dic[sortedstr] = [str] if sortedstr not in dic else dic[sortedstr]+[str]
        print(dic)
        res=[]
        for value in dic.values():
            res.append(value)
        return res

        # dict = {}
        # for word in strs:
        #     sortedword = "".join(sorted(word))
        #     dict[sortedword] = [word] if sortedword not in dict else dict[sortedword] + [word]
        # print(dict)
        # result = []
        # for item in dict:
        #     result.append(dict[item])
        # return result





def execute():
    sol = Solution()
    x = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # x = ["", "b"]
    # print(sol.isPremuation('eat','tan'))
    # print(sol.isPremuation('', 'b'))
    print(sol.groupAnagrams(x))


if __name__ == '__main__':
    execute()
