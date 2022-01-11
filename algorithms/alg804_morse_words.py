# 804. Unique Morse Code Words (Easy)
# https://leetcode.com/problems/unique-morse-code-words/
#
# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:
# "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cba" can be written as "-.-..--...",
# (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.
#
# Return the number of different transformations among all words we have.
#
# Example:
#   Input: words = ["gin", "zen", "gig", "msg"]
#   Output: 2
#       "gin" -> "--...-."
#       "zen" -> "--...-."
#       "gig" -> "--...--."
#       "msg" -> "--...--."


class Solution:
    # ---------------------------------------------------------------
    #       Main Solution
    # ---------------------------------------------------------------
    def uniqueMorseRepresentations(self, words):
        """

        :param words: List[str])
        :return: int
        """
        code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
                "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
                "..-", "...-", ".--", "-..-", "-.--", "--.."]

        letter = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        morse = {letter[i]: code[i] for i in range(len(letter))}
        unique_codes = {"".join(morse[c] for c in word) for word in words}

        return len(unique_codes)

    # ---------------------------------------------------------------
    #       Alternate Recursive Solution
    # ---------------------------------------------------------------
    def uniqueMorseRepresentations_alt(self, words):
        """

        :param words: List[str])
        :return: int
        """
        code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
                "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
                "..-", "...-", ".--", "-..-", "-.--", "--.."]

        unique_codes = {"".join(code[ord(c) - ord('a')] for c in word) for word in words}

        return len(unique_codes)


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    in1 = ["gin", "zen", "gig", "msg"]
    out1 = 2

    my_in, my_out = in1, out1
    print("Input    : %s" % (my_in))
    print("Expected : %s" % (my_out))
    print()

    # out = sol.uniqueMorseRepresentations(my_in)
    out = sol.uniqueMorseRepresentations_alt(my_in)
    print("Output : %s" % (out))
