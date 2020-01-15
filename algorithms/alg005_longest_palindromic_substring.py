# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

# Problem:
#   Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example:
#   Input: "babad"
#   Output: "bab", "aba" is also a valid answer.


import typing


class Solution:

    # -----------------------------------------------------------------
    def isPalindromic(self, s: str) -> bool:
        if len(s) % 2 == 0:
            # Even Length
            lm = len(s) // 2
            subL = s[0:lm]
            subR = s[-1:lm - 1:-1]
        else:
            # Odd Length
            lm = (len(s) - 1) // 2
            subL = s[0:lm]
            subR = s[-1:lm:-1]

        return subL == subR

    # -----------------------------------------------------------------
    def expandAroundCenter(self, s, left, right):
        # Shift Index to Sides
        L = left
        R = right

        # Expand until symmetric
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1

        # Length of final one
        return R - L - 1

    # -----------------------------------------------------------------
    #   Brute Force (Longer)
    # -----------------------------------------------------------------
    def longestPalindrome_bf(self, s: str) -> str:
        length = len(s)
        if (length < 1): return s

        maxlen = 0
        maxsub = ""
        # Loop over starting index of i, find longest Palindromic
        for i in range(length):
            j = length
            while j > i:
                if self.isPalindromic(s[i:j]):
                    # print ("breaking at i,j=",i,j, s[i:j])
                    break
                j -= 1

            if (j + 1 - i) > maxlen:
                maxlen = (j + 1 - i)
                maxsub = s[i:j]
        return maxsub

    # -----------------------------------------------------------------
    #   Dynamic algorithms (Faster)
    # -----------------------------------------------------------------
    def longestPalindrome(self, s):

        length = len(s)
        if (length < 1): return s

        start = 0
        end = 0
        for i in range(0, length):

            len_odd = self.expandAroundCenter(s, i, i)
            len_even = self.expandAroundCenter(s, i, i + 1)
            lenm = max(len_odd, len_even)
            if lenm > end - start:
                start = i - (lenm - 1) // 2
                end = i + lenm // 2
        return s[start: end + 1]


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()

    # print (sol.isPalindromic("bab"))
    # print (sol.longestPalindrome("babad"))
    print(sol.longestPalindrome_alt("babad"))
