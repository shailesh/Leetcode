# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l=[]
        head=point=ListNode(0)
        for i in lists:
            while(i!=None):
                heappush(l,i.val)
                i=i.next
        while(len(l)>0):
            point.next=ListNode(heappop(l))
            point=point.next
        return head.next