# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        """
        Time: O(max(n, m)), where n is length of l1 and m the length of l2
        Space: O(max(n, m))
        """
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            curr_sum = v1 + v2 + carry
            carry = curr_sum // 10
            curr_sum = curr_sum % 10

            curr.next = ListNode(curr_sum)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
