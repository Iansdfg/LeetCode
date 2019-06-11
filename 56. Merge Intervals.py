class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda x: x[0])
        ret = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= ret[-1][1]:
                ret[-1][1] = max(ret[-1][1], interval[1])
            else:
                ret.append(interval)
            print(ret)
        return ret

def execute():
    sol = Solution()
    intervals = [[1, 6], [5, 2], [8, 10], [15, 18]]
    print(sol.merge(intervals))

if __name__ == '__main__':
    execute()

