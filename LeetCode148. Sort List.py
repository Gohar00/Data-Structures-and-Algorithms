# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        nums = []
        current = head
        while current:
            nums.append(current.val)
            current = current.next
        
        nums.sort()
        sorted_head = ListNode(nums[0])
        current = sorted_head
        for i in range(1, len(nums)):
            current.next = ListNode(nums[i])
            current = current.next
        return sorted_head
