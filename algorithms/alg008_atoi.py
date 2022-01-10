# 8. String to Integer (Medium)
# https://leetcode.com/problems/string-to-integer-atoi/
#
# Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters as necessary until the first
# non-whitespace character is found. Then, starting from this character, takes an optional
# initial plus or minus sign followed by as many numerical digits as possible, and interprets
# them as a numerical value.
#
# The string can contain additional characters after those that form the integral number,
# which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters,
# no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
#
#   Only the space character ' ' is considered as whitespace character.
#   Assume we are dealing with an environment which could only store integers within the 32-bit
#   signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable
#   values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
#
# Examples:
#     Input: "   -42"
#     Output: -42
#     Explanation: The first non-whitespace character is '-', which is the minus sign.
#                  Then take as many numerical digits as possible, which gets 42.
#
#     Example 3:
#
#     Input: "4193 with words"
#     Output: 4193
#     Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
#
#     Example 4:
#
#     Input: "words and 987"
#     Output: 0
#     Explanation: The first non-whitespace character is 'w', which is not a numerical
#                  digit or a +/- sign. Therefore no valid conversion could be performed.


class Solution:

    def myAtoi(self, s):
        chars_valid = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        signs_valid = ['+', '-']

        digits = []
        is_signed = 0
        s = s.strip()

        seq = False
        i = 0
        while i < len(s):
            if s[i] == ' ' and seq:
                break
            elif s[i] in signs_valid and not seq:
                seq = True
                if s[i] == '+':
                    is_signed = 1
                else:
                    is_signed = -1
            elif s[i] in chars_valid:
                seq = True
                digits.append(int(s[i]))
            else:
                break
            i += 1

        num = 0
        mlt = 1
        for j in digits[-1::-1]:
            if is_signed < 0 and -2 ** 31 > -1 * (num + j * mlt):
                # return - 2**31
                num = -2 ** 31
                return num

            elif is_signed >= 0 and (num + j * mlt) > 2 ** 31 - 1:
                # return + 2**31 -1
                num = 2 ** 31 - 1
                return num
            else:
                num += j * mlt
                mlt *= 10

        if is_signed != 0:
            num = is_signed * num

        return num


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    # print(sol.myAtoi(" +-13"))
    # print(sol.myAtoi(" -123 3456 word "))
    print(sol.myAtoi("-2147483648"))
    # print(sol.myAtoi("2147483647"))

