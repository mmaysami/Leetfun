# 763. Partition Labels (Medium)
# https://leetcode.com/problems/partition-labels/
#
# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
# Return a list of integers representing the size of these parts.
#
# Examples:
#   Input: s = "ababcbacadefegdehijhklij"
#   Output: [9,7,8]
#   Explanation: The partition is "ababcbaca", "defegde", "hijhklij".
#   This is a partition so that each letter appears in at most one part.
#   A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
#
#   Input: s = "eccbbbbdec"
#   Output: [10]
#
# Constraints:
#   1 <= s.length <= 500
#   s consists of lowercase English letters.


class Solution:
    # ---------------------------------------------------------------
    # Main Solution: Hash(max index), loop with pointer to max of char
    # ---------------------------------------------------------------
    def partitionLabels(self, s: str):  # -> list[int]
        hash_dict = {}
        n = len(s)
        for i in range(n):
            hash_dict[s[i]] = i

        # List of Partition Length
        res = []

        # Index Pointer to Partitions
        i = 0
        while (i < n):
            ind_start = i
            j = i + 1
            ind_last = hash_dict[s[i]]

            # Loop over start to max index for other characters and their last index
            while (j <= ind_last):
                # Update ind_last of partition
                if hash_dict[s[j]] > ind_last:
                    ind_last = hash_dict[s[j]]
                j += 1

            # Partition complete, append length
            res.append(j - ind_start)

            # Jump pointer to next character after partition end
            i = j
        return res

    # ---------------------------------------------------------------
    #  Alt Solution:  Hash(Char: min_ind, max_ind), Sort, Merge Intervals
    # ---------------------------------------------------------------
    def partitionLabels_alt(self, s: str):  # -> list[int]
        hash_dict = {}
        for i in range(len(s)):
            # Hash of letter: [min index, max index]
            if s[i] in hash_dict:
                hash_dict[s[i]][1] = i
            else:
                hash_dict[s[i]] = [i, i]

        # Sort Index intervals for each letter by start
        intervals = list(hash_dict.values())
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        # Merge Overlapping Intervals
        for i in range(1, len(intervals)):
            if intervals[i][0] < res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])

        return [e[1] - e[0] + 1 for e in res]


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    in1 = "ababcbacadefegdehijhklij"
    out1 = [9, 7, 8]

    in2 = "eccbbbbdec"
    out2 = [10]

    my_in, my_out = in1, out1
    print("Input    : %s" % (my_in))
    print("Expected : %s" % (my_out))
    print()

    out = sol.partitionLabels(my_in)
    out_alt = sol.partitionLabels_alt(my_in)
    print("Output : %s" % (out))
    print("Alt Out: %s" % (out_alt))
