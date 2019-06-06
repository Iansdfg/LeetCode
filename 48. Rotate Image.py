class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i>j:
                    matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(n):
            l, r = 0, n - 1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l+=1
                r-=1

def execute():
    sol = Solution()
    matrix = [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
    ]
    print(sol.rotate(matrix))
    print(matrix)

if __name__ == '__main__':
    execute()

