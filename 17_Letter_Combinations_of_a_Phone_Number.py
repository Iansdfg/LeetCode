class Solution(object):
    def letterCombinations(self,digits):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dic = {'0': '',
               '1': '*',
               '2': 'abc',
               '3': 'def',
               '4': 'ghi',
               '5': 'jkl',
               '6': 'mno',
               '7': 'pqrs',
               '8': 'tuv',
               '9': 'wxyz',
        }
        results = []
        for digit in digits:
            if len(results) == 0:
                for letter in dic[digit]:
                    results.append(letter)
            else:
                tempResults = []
                for result in results:
                    for letter in dic[digit]:
                        tempResults.append(result + letter)
                results = tempResults
        return results

def execute():
    sol = Solution()

    digits = '23'
    print(sol.letterCombinations(digits))

if __name__ == '__main__':
    execute()

