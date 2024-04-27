# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        is_runing = True
        s = 0
        res = ListNode(s)
        first_res = res

        while is_runing:
            if l1 is not None:
                s += l1.val
                l1 = l1.next

            if l2 is not None:
                s += l2.val
                l2 = l2.next
            
            res.val = s % 10
            s = s // 10

            if l1 is None and l2 is None and s == 0:
                is_runing = False
            else:
                res.next = ListNode(s)
                res = res.next

        
        res = first_res

        return res