# Look and Say
# https://www.facebook.com/careers/life/sample_interview_questions/Af8BaL90PrQGVj_YuGqVdJhmgdeuj-dq1vO9gy4HAmrDRNAglybwgdtN55L5_rICwCY


def look_and_say(n):
    """
    Return n-th element of Look-and-Say Sequence as string
    https://en.wikipedia.org/wiki/Look-and-say_sequence
    1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, …
    """

    # Base Cases
    if n == 1:
        cur = str(1)
    elif n == 2:
        cur = str(11)
    else:
        # Other Cases (Semi-Recursive)
        prev = "11"
        # Form elements 3 .. n of the sequence
        for k in range(3, n + 1):
            # Init previous and current elements
            prev += "#"
            cur = ""
            cnt = 1

            # Loop over length and count sequences of characters
            for i in range(1, len(prev)):
                if prev[i] == prev[i - 1]:
                    cnt += 1
                else:
                    cur += str(cnt) + prev[i - 1]
                    cnt = 1

            prev = cur
    return cur


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    for n in range(1, 20):
        sol = look_and_say(n)
        print(sol)
