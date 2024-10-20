# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next==None:
            return head
        i,j=head,head.next
        s,prev=j.next,None
        brk=True
        while brk:
            if j.next is None:brk=False
            i.next=prev
            s=j.next
            j.next=i
            prev=j
            if s is None:
                return j
            else:
                i=s
            if i.next is None:
                i.next=prev
                return i
            else:
                j=i.next
        return j
            