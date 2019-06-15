class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:return 0
        citations.sort()
        citations[:] = citations[::-1]
        print(citations)
        for i in range(len(citations)):
            if i >= citations[i]:
                return i
        return len(citations)
        
