# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
#
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
# Example 2:
# Input: digits = ""
# Output: []
#
# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]
#
# Constraints:
#     0 <= digits.length <= 4
#     digits[i] is a digit in the range ['2', '9'].

class Solution:

    def letterCombinations(self, digits: str) -> list:
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return list(d.get(digits, ''))
        else:
            current = self.letterCombinations(digits[:-1])
            last = list(d.get(digits[-1], ''))

            combo = []
            for e in last:
                combo += [c + e for c in current]
            return combo

    def letterCombinations_alt(self, digits: str) -> list:

        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        stack = []

        if digits == "": return stack

        def back(i, currstr):
            if len(currstr) == len(digits):
                stack.append(currstr)
                return  # base case

            for c in d[digits[i]]:
                back(i + 1, currstr + c)
        back(0, "")
        return stack


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations_alt("23"))
