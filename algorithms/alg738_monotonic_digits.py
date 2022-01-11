# 738. Monotone Increasing Digits (Medium)
# https://leetcode.com/problems/monotone-increasing-digits/
#
# An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.
# Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.
#
# Example:
#   Input: n = 10
#   Output: 9
#
#   Input: n = 1234
#   Output: 1234
#
#   Input: n = 332
#   Output: 299


class Solution:
    """
    666624 --> 555599
    Loop reverse, compare each digit with left side if not valid, left -=1, digit:end=9
    """
    # ---------------------------------------------------------------
    #       Main Solution
    # ---------------------------------------------------------------
    def monotoneIncreasingDigits(self, n: int) -> int:
        """
            2   4   4    3
                <--i  i+1   step1 : check s[i] <= s[i+1], until s[i] > s[i+1]
            2   4   3   9
                            step2 : s[i]-=1, change all s[i+1:] into '9'

            <--i  i+1       Repeat step1/2 toward left of digits
            2  3    9   9
        """

        # Form List of Digit Strings
        digit_list = list(str(n))

        # Reverse Sweep Digits from Right to Left
        for i in range(len(digit_list)-2, -1, -1):
            if digit_list[i] <= digit_list[i+1]:
                continue
            else:
                digit_list[i] = str(int(digit_list[i])-1)
                digit_list[i+1:] = ['9'] * len(digit_list[i+1:])

        return int(''.join(digit_list))

# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    ins = [6, 10, 333, 332, 334, 2443, 666634, 666633]
    outs = [6, 9, 333, 299, 334, 2399, 599999, 599999]

    for case in range(len(ins)):
        my_in, my_out = ins[case], outs[case]
        print("Input    : %s" % (my_in))
        print("Expected : %s" % (my_out))

        out = sol.monotoneIncreasingDigits(my_in)
        print("Output   : %s" % (out))
        print()
