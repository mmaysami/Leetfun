# 20. Valid Parenthesis (Easy)
# https://leetcode.com/problems/valid-parentheses/
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#
# Examples:
#     Input: "()[]{}"
#     Output: true
#
#     Input: "([)]"
#     Output: false
#
#     Input: "{[]}"
#     Output: true


import re


class Solution:
    # ------------------------------------------------------------------------
    def isValid(self, s):
        """ Use LIFO Operation of Stacks"""
        from collections import deque

        dict_pair = {'(': ')', '[': ']', '{': '}'}
        char_open = {'(', '[', '{'}
        char_close = {')', ']', '}'}

        que = deque()

        for c in s:
            if c in char_open:
                que.append(c)
            elif c in char_close:
                if not que:
                    return False
                else:
                    pair = que.pop()
                    if dict_pair[pair] != c: return False

        if que:
            return False

        return True

    # ------------------------------------------------------------------------
    def isValid_alt(self, s):
        """
        # Given an input string (s) and a pattern (p), implement regular expression matching
        #   with support for '.' and '*'.
        #   '.' Matches any single character.
        #   '*' Matches zero or more of the preceding element.
        #   The matching should cover the entire input string (not partial).
        #
        # Note:
        #     s could be empty and contains only lowercase letters a-z.
        #     p could be empty and contains only lowercase letters a-z, and characters like . or *.

        :param s:
        :return:
        """
        # Validate w.r.t. description [Optional]
        valid_s = r'^[\[|\]|\(|\)|\{|\}]*$'

        if re.match(valid_s, s) is None:
            print("s is not valid!")
            return False

        dict_pair = {'(': ')', '[': ']', '{': '}'}
        char_open = {'(', '[', '{'}
        char_close = {')', ']', '}'}
        order = []

        valid = True
        for i in range(len(s)):
            if s[i] in char_open:
                order.append(s[i])
            elif s[i] in char_close:
                if len(order) == 0:
                    valid = False
                    break
                elif dict_pair[order[-1]] == s[i]:
                    order.pop(-1)
                else:
                    valid = False
                    break

        if len(order) > 0:
            valid = False
        return valid


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()[]{}"), "Expected: True")
    print(sol.isValid("{[]}"), "Expected: True")
    print(sol.isValid("()[]{"), "Expected: False")
    print(sol.isValid("())"), "Expected: False")
    print(sol.isValid("([)]"), "Expected: False")
