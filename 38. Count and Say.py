class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        """
        1.     1
        2.     11
        3.     21
        4.     1211
        5.     111221
        """
        res = '1'
        for i in range(n-1):
            string = ''
            j = 0
            while j < len(res):
                count = 1
                while len(res)>j+1 and res[j] == res[j+1]:
                    count += 1
                    j += 1
                string += str(count) + res[j]
                j += 1
            res = string
        return res



def execute():
    sol = Solution()
    n = 5
    print(sol.countAndSay(n))

if __name__ == '__main__':
    execute()

