# 937. Reorder Data in Log Files
# https://leetcode.com/problems/reorder-data-in-log-files/
#
# You have an array of logs.  Each log is a space delimited string of words.
# For each log, the first word in each log is an alphanumeric identifier.  Then, either:
#   - Each word after the identifier will consist only of lowercase letters, or;
#   - Each word after the identifier will consist only of digits.
#
# We will call these two varieties of logs letter-logs and digit-logs. It is guaranteed that each log has at least one word after its identifier.
# Reorder the logs so that all the *letter-logs* come before any digit-log.
#   - The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.
#   - The digit-logs should be put in their original order.

# Return the final order of the logs.
#
# Constraints:
#     0 <= logs.length <= 100
#     3 <= logs[i].length <= 100
#     logs[i] is guaranteed to have an identifier, and a word after the identifier.
#
# Examples:
#   Input:  ["dig1 8 1 5 1", "let1 art can",  "dig2 3 6",         "let2 own kit dig", "let3 art zero"]
#   Output: ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1",     "dig2 3 6"]


class Solution:

    # ---------------------------------------------------------------
    #       Main Solution
    # ---------------------------------------------------------------
    def reorderLogFiles(self, logs):
        def f_keys(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key=f_keys)

    # ---------------------------------------------------------------
    #       Alternate Solution
    # ---------------------------------------------------------------
    def reorderLogFiles_alt(self, logs):
        llogs = filter(lambda l: l.split(" ", 1)[1].isalpha(), logs)
        dlogs = filter(lambda l: l.split(" ", 1)[1].isdigit(), logs)
        return sorted(llogs, key=lambda x: (x.split(" ")[1:], x.split(" ")[0])) + list(dlogs)


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    in1 = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    out1 = ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]

    in2 = []
    out2 = []

    my_in, my_out = in1, out1
    print("Input    : %s" % (my_in))
    print("Expected : %s" % (my_out))
    print()

    out = sol.reorderLogFiles(my_in)
    print("Output : %s" % (out))
