# 46. Permutations
# https://leetcode.com/problems/permutations/
#
# Given a collection of distinct integers, return all possible permutations.
#
# Examples:
#
#     Input: [1,2,3]
#     Output:
#     [
#       [1,2,3],
#       [1,3,2],
#       [2,1,3],
#       [2,3,1],
#       [3,1,2],
#       [3,2,1]
#     ]
#
# Note:
#     1. Think of string as a graph, where each character is connected to every other character
#     2. Instead of trying to find a "path" from source to destination, frame the problem as follows:
#           "find all paths of a specific length - from every source"


from math import factorial


class Solution:
    # ---------------------------------------------------------------
    #       Main Solution
    # ---------------------------------------------------------------
    def permute(self, nums):
        length = len(nums)

        if length == 1:
            res = [nums]
        else:
            # Get all sub permutations
            sub_perm = []
            pre = []
            for i in range(length):
                sub_perm += self.permute(nums[1:i]+nums[i+1::])
                # pre += factorial(length - 1) * [ [ nums[i] ] ]

            # print("Nums: ", nums)
            # print("Len: %s,  Factorial: %s" %(length, factorial(length)))
            # print("Len Perm: ", len(sub_perm))
            # print("Len Pre: ", len(pre))
            # print('--'*40)
            # res = [pre[i] + e for i, e in enumerate(sub_perm)]

            res = sub_perm
        return res

    # ---------------------------------------------------------------
    #       Graph DFS Solution
    # ---------------------------------------------------------------
    def permute_dfs(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # Back

        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    lst = [1, 2, 3]
    print("List : ", lst)
    print("Result : \n", sol.permute(lst))
