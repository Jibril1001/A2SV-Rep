# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ls=[]
        ls.append(head.val)
        while head.next:
            head=head.next
            ls.append(head.val)
        i,j=0,len(ls)-1
        print(ls)
        while i<=j:
            if ls[i]!=ls[j]:
                return False
            i+=1
            j-=1
        return True