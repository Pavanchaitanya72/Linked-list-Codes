Split Linked List in Parts
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length=0
        curr=head
        while curr:
            length+=1
            curr=curr.next
        Q,Rem=divmod(length,k)
        a=[]
        temp=head
        for i in range(k):
            dummy=write=ListNode(0)
            for j in range(Q+(i<Rem)):
                if temp:
                    write.next=write=ListNode(temp.val)
                    temp=temp.next
            a.append(dummy.next)
        return a
            

        
        