class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
#         dic = {}
#         for char in s:
#             if char in dic:
#                 dic[char]+=1
#             else:
#                 dic[char] = 1
#         for char in t:
#             if char in dic:
#                 dic[char]-=1
#             else:
#                 return False
#         for key in dic:
#             if dic[key]!= 0:
#                 return False
#         return True
        if len(set(s))!=len(set(t)):
            return False
        for i in set(s):
            if s.count(i)!=t.count(i):
                return False
        return True
        
