# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/
#
# Given a 32-bit signed integer, reverse digits of an integer.
# Assume we are dealing with an environment which could only store integers within
# the 32-bit signed integer range: [−231,  231 − 1].
# For the purpose of this problem, assume that your function returns 0
# when the reversed integer overflows.
#
# https://leetcode.com/problems/reverse-integer/
#
# Examples:
#
#     Input: 123
#     Output: 321
#
#     Input: -123
#     Output: -321
#
#     Input: 120
#     Output: 21


class Solution:
    def reverse(self, x):
        digits = []

        if x < 0:
            neg = -1
            x = -x
        else:
            neg = +1

        dv = 10
        while x > 0:
            digits.append(x % dv)
            x = x // dv

        # print(digits)
        y = 0
        dv = 1
        for i in range(len(digits) - 1, -1, -1):
            # print(y)
            if -1 * 2 ** 31 <= neg * (y + dv * digits[i]) <= 2 ** 31 - 1:
                y += dv * digits[i]
                dv *= 10
            else:
                y = 0
                break

        y = neg * y
        return y


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(-123))
