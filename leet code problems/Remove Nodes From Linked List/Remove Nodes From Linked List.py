 Remove Nodes From Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        dummy=headNew=ListNode(None,head)
        cur=head
        while cur:
            while stack and stack[-1].val<cur.val:
                stack.pop()
            stack.append(cur)
            cur=cur.next
        
        for node in stack:
            headNew.next=node
            headNew=headNew.next
        return dummy.next


