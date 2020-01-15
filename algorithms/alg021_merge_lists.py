# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
#
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

# Examples:
#
# Input: 1->2->4,   1->3->4
# Output: 1->1->2->3->4->4


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def list2nodes(cls, lst):
        nextnode = None
        for v in lst[-1::-1]:
            node = cls(v)
            node.next = nextnode
            nextnode = node

        return node

    def nodes2list(self):
        ll = []
        n = self
        while n is not None:
            ll.append(n.val)
            n = n.next
        return ll


class Solution:
    def mergeTwoLists(self, l1, l2):
        ml_start = ListNode(0)
        ml = ml_start

        # Sweep over nodes of l1 and l2
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                ml.next = ListNode(l1.val)
                l1 = l1.next
            else:
                ml.next = ListNode(l2.val)
                l2 = l2.next
            ml = ml.next

        # Nodes remaining from l1 xor l2
        if not l1:
            ml.next = l2
        elif not l2:
            ml.next = l1

        return ml_start.next


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()

    l1 = ListNode.list2nodes([1, 2, 4])
    l2 = ListNode.list2nodes([1, 3, 4])

    print(l1.nodes2list())
    print(l2.nodes2list())
    print(sol.mergeTwoLists(l1, l2).nodes2list())
