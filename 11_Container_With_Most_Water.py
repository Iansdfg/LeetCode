class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        max = 0
        while left < right:
            if height[left] > height[right]:
                lower = height[right]
            else:
                lower = height[left]
            if (right - left) * lower > max:
                max = (right - left) * lower
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max

def execute():
    sol = Solution()
    s = [1,8,6,2,5,4,8,3,7]
    s = [2, 1]
    # # s = [1, 1]
    # # s = [1, 2]
    # s = [1,2,4,3]
    print(sol.maxArea(s))

if __name__ == '__main__':
    execute()
