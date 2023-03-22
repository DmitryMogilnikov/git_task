from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = head = ListNode()
        residue = 0
        while l1 or l2 or residue:
            sum_node = residue
            if l1:
                sum_node += l1.val
                l1 = l1.next
            if l2:
                sum_node += l2.val
                l2 = l2.next

            residue, sum_node = divmod(sum_node, 10)
            head.next = ListNode(sum_node)
            head = head.next
        return result.next
    
if __name__ == "__main__":
    l1 = ListNode()
    l2 = ListNode()
    for i in range(3):
        l1 = ListNode(i)
        l2 = ListNode(2 * i)
        l1 = l1.next
        l2 = l2.next
        Solution.add_two_numbers(l1,l2)