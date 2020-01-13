# 6. Zig Zag Conversation
# https://leetcode.com/problems/zigzag-conversion/

# Problem:
#   The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this
#   string convert(string s, int numRows)

# Example: DOWN - DIAGONAL UP.RIGHT - DOWN ...
# Input: "PAYPALISHIRING"
#
#   P   A   H   N
#   A P L S I I G
#   Y   I   R
#
# Output:   line by line: "PAHNAPLSIIGYIR"


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lines = [[] for i in range(numRows)]
        length = len(s)

        lnmap = list(range(numRows)) + list(range(numRows - 2, 0, -1))
        for i, c in enumerate(s):
            l = i % len(lnmap)
            # print(i,lnmap[l])
            lines[lnmap[l]].append(c)

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
