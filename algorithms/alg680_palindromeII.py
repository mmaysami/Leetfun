# 680. Valid Palindrome II [FB] (Easy)
# https://leetcode.com/problems/valid-palindrome-ii/
# Given a string s, return true if the s can be palindrome after
# deleting at most one character from it.
# A string is a palindrome when it reads the same backward as forward.
#
# Constraints:
#     1 <= s.length <= 105
#     s consists of lowercase English letters.
#
# Examples:
#   Input: s = "aba"
#   Output: true
#
#   Input: s = "abca"
#   Output: true
#   Explanation: You could delete the character 'c'.
#
#   Input: s = "abc"
#   Output: false

import typing

class Solution:
    def is_palindrome(self, s: str) -> bool:
        return str(s) == str(s)[::-1]

    def valid_palindrome(self, s: str) -> bool:
        if len(s) < 3: return True
        if len(s) == len(set(s)): return False

        if self.is_palindrome(s): return True

        for i,c in enumerate(s):
            if self.is_palindrome(s[:i]+s[i+1:]): return True
        return False


    # def is_palindrome_alt(self, s, l, h):
    #     if l < h:
    #         if s[l] == s[h]:
    #             return self.is_palindrome(s, l + 1, h - 1)
    #         else:
    #             return False
    #     return True

    # def valid_palindrome_alt(self, s: str) -> bool:
    #     if len(s) < 3: return True
    #     if len(s) == len(set(s)): return False
    #
    #     l = 0
    #     r = len(s) - 1
    #
    #     while l < r:
    #         if s[l] == s[r]:
    #             l += 1
    #             r -= 1
    #         else:
    #             if self.is_palindrome(s, l + 1, r) or self.is_palindrome(s, l, r - 1):
    #                 return True
    #             return False
    #     return True


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("abc"))
    print(sol.isPalindrome("abca"))
    print(sol.isPalindrome_q("a"))
