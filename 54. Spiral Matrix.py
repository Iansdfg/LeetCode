class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]: return []
        res = []
        direct = 0
        up, left, down, right = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        while True:
            if direct == 0:
                for i in range(left, right+1):
                    res.append(matrix[up][i])
                up += 1

            if direct == 1:
                for i in range(up, down+1):
                    res.append(matrix[i][right])
                right -= 1

            if direct == 2:
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                down -= 1

            if direct == 3:
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
                left += 1

            if up > down or left > right: return res

            direct = (direct + 1) % 4




def execute():
    sol = Solution()
    matrix = [[1,11],
              [2,12],
              [3,13],
              [4,14],
              [5,15],
              [6,16],
              [7,17],
              [8,18],
              [9,19],
              [10,20]]
    print(sol.spiralOrder(matrix))

if __name__ == '__main__':
    execute()

