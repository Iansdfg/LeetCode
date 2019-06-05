class Solution(object):

    def generateParenthesisDFS(self,left,right,item,res):
        print(item, res)
        if right<left:
            return
        if left == 0 and right ==0:
            res.append(item)
        if left>0:
            self.generateParenthesisDFS(left-1,right,item+'(',res)
        if right>0:
            self.generateParenthesisDFS(left, right - 1, item + ')', res)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return []
        res=[]
        self.generateParenthesisDFS(n,n,'',res)
        return res


def execute():
    sol = Solution()
    n = 3
    print(sol.generateParenthesis(n))



if __name__ == '__main__':
    execute()



