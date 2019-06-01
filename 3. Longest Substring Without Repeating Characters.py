class Solution(object):
    def lengthOfLongestSubstring(self, s):
        target = ''
        longest = ''
        for letter in s:
            if letter not in target:
                target += letter
            else:
                target = target.split(letter)[-1]
                target += letter
            if len(target)>len(longest):
                longest = target
        return len(longest)


        # targetString=''
        # longestString=''
        # for letter in s:
        #     if letter not in targetString:
        #         targetString += letter
        #     else:
        #         targetString = targetString.split(letter)[-1]
        #         targetString += letter
        #     if len(targetString) > len(longestString):
        #         longestString = targetString
        # return len(longestString)

def execute():
    sol = Solution()
    s = 'abcabcbb'
    print(sol.lengthOfLongestSubstring(s))

if __name__ == '__main__':
    execute()

