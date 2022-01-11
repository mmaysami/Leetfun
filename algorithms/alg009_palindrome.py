# 9. Palindrome Number (Easy)
# https://leetcode.com/problems/palindrome-number/
#
# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is palindrome while 123 is not.
#
# Constraints:
#     -2**31 <= x <= 2**31 - 1
#
# Examples:
#   Input: x = 121
#   Output: true
#
#   Input: x = -121
#   Output: false
#   Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#
#   Input: x = 10
#   Output: false
#   Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#   Input: x = -101
#   Output: false

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Using String Reversal"""
        if x < 0:
            return False
        elif x < 10:
            return True

        return str(x) == str(x)[::-1]

    def isPalindrome_ptr(self, x: int, l:int=0, r:int=-1):
        """Using Two Pointers"""
        x = str(x)
        if r==-1: r = len(x) - 1
        if l < r:
            if x[l] == x[r]:
                return self.isPalindrome_ptr(x, l + 1, r - 1)
            else:
                return False
        return True

    def isPalindrome_q(self, x: int) -> bool:
        """Using Priority Queue"""
        from collections import deque
        q = deque(str(x))
        while q:
            right_digit = q.pop()
            if q:
                left_digit = q.popleft()
                if left_digit != right_digit:
                    return False
        return True


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    tests = [-797, 1234321, 2112, 8]
    for case in tests:
        print("Input: {:15}, Reverse {}".format(case, sol.isPalindrome(case)))
        print("Input: {:15}, Pointer {}".format(case, sol.isPalindrome_ptr(case)))
        print("Input: {:15}, Queue   {}".format(case, sol.isPalindrome_q(case)))
