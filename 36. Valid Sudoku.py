class Solution:
    def rowValid(self, list):
        dic = []
        for ele in list:
            if ele == ".":
                continue
            if ele in dic:
                return False
            else:
                dic.append(ele)
        return True

    def columnValid(self,lists,nth):
        dic = []
        for list in lists:
            if list[nth] == ".":
                continue
            if list[nth] in dic:
                return False
            else:
                dic.append(list[nth])
        return True

    def oneBlockValid(self,lists,i,j):
        dic=[]
        for i in range(i,i+3):
            k = j
            for k in range(k,k+3):
                # print(i,j)
                # print(lists[i][j])
                if lists[i][k] == ".":
                    continue
                if lists[i][k] in dic:
                    return False
                else:
                    dic.append(lists[i][k])
        return True

    def BlockValid(self, lists):
        res = True
        for i in range(0,9,3):
            for j in range(0,9,3):
                res *=self.oneBlockValid(lists,i,j)
        return bool(res)

    def isValidSudoku(self, board):
        res = 1
        for row in board:
            res *= self.rowValid(row)

        for i in range(len(board[0])):
            res *= self.columnValid(board,i)
        res *= self.BlockValid(board)
        return bool(res)



def execute():
    sol = Solution()
    x = [
[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]]


    print(sol.columnValid(x,0))
    print(sol.oneBlockValid(x,0,0))
    print(sol.BlockValid(x))
    print(sol.isValidSudoku(x))


if __name__ == '__main__':
    execute()

