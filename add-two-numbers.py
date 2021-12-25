class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        remem = 0  # carry

        res = ListNode(0)
        head = res
        while l1 or l2 or remem > 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            s = l1Val + l2Val + remem
            digit = s % 10
            remem = s // 10
            res.val = digit
            if (l1 and l1.next) or (l2 and l2.next) or remem > 0:
                res.next = ListNode(0)
                res = res.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return head
