# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        c1=head
        c2=head
        if head==None:
            return False
        if c1.next==None:
            return False
        while c1!=None and c2!=None and c1.next and c2.next and c2.next.next:
            c1=c1.next
            c2=c2.next.next
            if c1==c2:
                return True
        return False