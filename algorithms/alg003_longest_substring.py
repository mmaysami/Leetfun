# 3. Longest Substring Without Repeating Characters  (Medium)
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# Problem:
#   Given a string, find the length of the longest substring without repeating characters
#
# Example:
#   Input: "abcabcbb"
#   Output: 3
#   Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
#   Input: "bbbbb"
#   Output: 1
#   Explanation: The answer is "b", with the length of 1.

import typing


class Solution:

    # ---------------------------------------------------------------
    #       Main Solution
    # ---------------------------------------------------------------
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s = s.lower()  # CASE SENSITIVE
        length = len(s)

        # Empty or Single Char String
        if length <= 1:
            return length

        maxsub = 0
        # Longer Strings
        for i in range(length):
            charset = set()
            j = i
            while (s[j] not in charset):
                charset.add(s[j])
                if j + 1 < length: j += 1

            if len(charset) > maxsub:
                maxsub = len(charset)

        return maxsub

    # ---------------------------------------------------------------
    #       Alternate Long Solution
    # ---------------------------------------------------------------
    def lengthOfLongestSubstring_alt(self, s: str) -> int:
        # s = s.lower()  # CASE SENSITIVE
        length = len(s)
        # Empty or Single Char String
        if length <= 1:
            return length

        # Longer Strings
        lensubs = [0]
        for b in range(length):
            if (length - b) < max(lensubs):
                break

            chars = []
            for i in range(b, length):
                if s[i] not in chars:
                    chars.append(s[i])
                else:
                    # print(b," : ", chars)
                    break
            lensubs.append(len(chars))

        return max(lensubs)


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))
