# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        
        while True:
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            group_next = kth.next

            prev = group_next
            curr = prev_group.next
            
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = prev_group.next
            prev_group.next = prev
            prev_group = temp
