# 25. Reverse Nodes in K-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/
#
# Given a linked list, reverse the nodes of a linked list k
# at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# Note:
#     - Only constant extra memory is allowed.
#     - You may not alter the values in the list's nodes, only nodes itself may be changed.
#
# Examples:
#
# Given this linked list: 1->2->3->4->5
# For k = 2, you should return: 2->1    ->4->3    ->5
# For k = 3, you should return: 3->2->1 ->4->5


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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Init Return and Current Node
        head_reverse = ListNode(-1)
        node_cur = head
        group_prev = []

        # Reverse Next Group
        while node_cur:
            group_cur = []
            i = 0

            # Get Next K Node (or last group)
            while i < k and node_cur:
                group_cur.append(node_cur)
                node_cur = node_cur.next
                i += 1
            # print([e.val for e in group_cur])

            # Skip if less than K node
            if len(group_cur) >= k:
                # Set Reverse List Head
                if not head_reverse.next:
                    # print("Assign New Head : ", group_cur[-1].val)
                    head_reverse.next = group_cur[-1]

                # Update Last Pointer of Last Group
                if len(group_prev)>0:
                    group_prev[0].next = group_cur[-1]
                group_prev = group_cur

                # Store Pointer to Next Group
                group_cur[0].next = group_cur[-1].next
                
                # Reverse Group Nodes
                for i in range(len(group_cur) - 1, 0, -1):
                    group_cur[i].next = group_cur[i - 1]

            # Case of List < k
            elif not head_reverse.next:
                head_reverse.next = group_cur[0]

        return head_reverse.next


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    k = 3
    l1 = [1, 2]

    # k = 2
    # l1 = [1, 2, 3, 4, 5]
    print("List : ", l1)
    print("k    : ", k)

    l1 = ListNode.list2nodes(l1)
    print("Result :", sol.reverseKGroup(l1, k).nodes2list())
