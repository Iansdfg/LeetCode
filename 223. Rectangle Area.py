class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if B>=H or E>=C or F>=D or A>=G:
            return (C-A) * (D-B) + (G-E) * (H-F)
        width = min(C,G) - max(A,E)
        height = min(D,H) - max(B,F)
        return (C-A) * (D-B) + (G-E) * (H-F) - width * height
