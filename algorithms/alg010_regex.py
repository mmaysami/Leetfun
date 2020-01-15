# 10. Regex Matching
# https://leetcode.com/problems/regular-expression-matching/
#
# Given an input string (s) and a pattern (p), implement regular expression matching
#       with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
# The matching should cover the entire input string (not partial).
#
# Note:
#
#     s could be empty and contains only lowercase letters a-z.
#     p could be empty and contains only lowercase letters a-z, and characters like . or *.
#
# Examples:
#    s = "aa"
#    p = "a"
#    Output: false
#
#     s = "ab"
#     p = ".*"
#     Output: true
#
#     s = "aab"
#     p = "c*a*b"
#     Output: true


import re


class Solution:
    def isMatch(self, s, p):

        # Validate s and p w.r.t description [Optional]
        valid_s = r'^[a-z]*$'
        valid_p = r'^[a-z\.\*]*$'

        if re.match(valid_s, s) is None:
            print("s is not valid!")
            return False

        if re.match(valid_p, p) is None:
            print("p is not valid!")
            return False

        # # Make p as entire string pattern
        # if len(p) == 0:
        #     p = "^$"
        # else:
        #     if p[0] != '^':
        #         p = '^' + p
        #     if p[-1] != '$':
        #         p = p + '$'
        #
        # # Find if s matches p
        # reg_p = re.compile(p)
        # match = reg_p.match(s)

        # Alternative (Use Full Match)
        reg_p = re.compile(p)
        match = reg_p.fullmatch(s)

        if match is None:
            return False
        else:
            return True


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    print(sol.isMatch("", ""))
    print(sol.isMatch("a", ""))
    print(sol.isMatch("aa", "a*"))
    print(sol.isMatch("ab", ".*"))
    print(sol.isMatch("aab", "c*a*b*"))
    print(sol.isMatch("aba", "c*a*b*"))
