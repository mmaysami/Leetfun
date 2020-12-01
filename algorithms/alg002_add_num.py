# 2. Add Two Numbers (Linked Lists)
# https://leetcode.com/problems/add-two-numbers/

# Problem:
#   two non-empty linked lists representing two non-negative integers
#   Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#   Output: 7 -> 0 -> 8
#   Explanation: 342 + 465 = 807


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # ---------------------------------------------------------------
    #       Main Solution
    # ---------------------------------------------------------------
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        co = 0  # Carry Over
        rl = []  # List of Results

        while (l1 != None) or (l2 != None) or (co != 0):
            if (l1 is None):
                l1 = ListNode(0)
                # l1.next = ListNode(0)
            if (l2 is None):
                l2 = ListNode(0)
                # l2.next = ListNode(0)

            ss = (l1.val + l2.val + co) % 10
            co = (l1.val + l2.val + co) // 10
            rn = ListNode(ss)  # Result ListNode
            rl.append(rn)  # List of Results

            l1 = l1.next
            l2 = l2.next

        rl = rl[::-1]  # Reverse Order of List of Results
        # print([e.val for e in rl])

        if len(rl) > 1:
            for i in range(1, len(rl)):
                rl[i].next = rl[i - 1]

        return rl[-1]

    # ---------------------------------------------------------------
    #       Alternate Recursive Solution
    # ---------------------------------------------------------------
    def addTwoNumbers_alt1(self, l1, l2, co=0):
        val = l1.val + l2.val + co
        co = val // 10
        r = ListNode(val % 10)

        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            r.next = self.addTwoNumbers(l1.next, l2.next, c)
        return r


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    # sol.addTwoNumbers()
