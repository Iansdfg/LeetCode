class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
        converDic = dict({ 1: "I",
                         5: "V",
                         10: "X",
                         50: "L",
                         100: "C",
                         500: "D",
                         1000: "M",
                           0: ''})
        div = 1000
        result = ''
        while div:
            if int(num/div) == 5:
                result += converDic[5 * div]
            elif int(num/div) == 9:
                result += converDic[div]+converDic[div*10]
            elif int(num/div) == 4:
                result += converDic[int(div)]+converDic[int(5 * div)]
            elif int(num/div) > 5:
                result += converDic[5 * div] + (int(num/div)-5)*converDic[div]
            else:
                result += int(num/div)*converDic[div]
            num = int(num%div)
            div = int(div/10)
        return result




def execute():
    sol = Solution()
    s = 1994
    print(sol.intToRoman(s))

if __name__ == '__main__':
    execute()

