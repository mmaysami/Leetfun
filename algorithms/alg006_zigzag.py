# 6. Zig Zag Conversation (Medium)
# https://leetcode.com/problems/zigzag-conversion/
#
# Problem:
#   The string "PAYPALISHIRING" is written in a zigzag pattern (DOWN - DIAGONAL UP.RIGHT - DOWN ...)
#   on a given number of rows like this string convert(string s, int numRows)
#
# Example:
#   DOWN - DIAGONAL UP.RIGHT - DOWN ...
#   Input: "PAYPALISHIRING"
#   Output:   line by line: "PAHNAPLSIIGYIR"
#   Explanation:
#       P   A   H   N
#       A P L S I I G
#       Y   I   R


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lines = [[] for i in range(numRows)]
        length = len(s)

        # Get Order of Lines for One Loop of Steps (Down, Diagonal Up-Right)
        lnmap = list(range(numRows)) + list(range(numRows - 2, 0, -1))
        for i, c in enumerate(s):
            l = i % len(lnmap)          # Find Loop Iteration of Character Index
            lines[lnmap[l]].append(c)   # Append Character to proper Line

        # Create Re-ordered String of Lines
        r = ''
        for l in lines:
            r += ''.join(l)
        return r


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 3))
