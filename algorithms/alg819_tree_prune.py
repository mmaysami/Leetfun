# 814. Binary Tree Pruning (Medium)
# https://leetcode.com/problems/binary-tree-pruning/
#
# Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
# A subtree of a node node is node plus every node that is a descendant of node.
#
# Examples
#   Input: root = [1,null,0,0,1]
#   Output: [1,null,0,null,1]
#   Explanation: Only the red nodes satisfy the property "every subtree not containing a 1".
#                The diagram on the right represents the answer.
#
#   Input: root = [1,0,1,0,0,0,1]
#   Output: [1,null,1,null,1]
#
#   Input: root = [1,1,0,1,1,0,1,0]
#   Output: [1,1,0,1,1,null,1]
#
# Constraints:
#     The number of nodes in the tree is in the range [1, 200].
#     Node.val is either 0 or 1.

import typing
from functools import reduce
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root):  # Optional[TreeNode]) -> Optional[TreeNode]
        """
        Use DFS-like and prune if a child branch is all zero

        Time  O(N): Each node (out of N nodes) is processed once.
        Space O(N): In skewed trees depth is number of nodes. the recursion call stack can be as large as the depth of tree.

        :param root:
        :return:
        """
        if not root:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        # Sub-Tree is pruned, keep if any child or value=1
        if root.left or root.right or root.val == 1:
            return root
        else:
            return None


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()

