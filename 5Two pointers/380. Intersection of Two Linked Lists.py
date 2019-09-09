"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        if not self.have_intersection(headA, headB):
            return None
        if headA == headB:
            return headA
            
        currA,currB = headA,headB
        while True:
            if currA.next:
                currA = currA.next 
            else:
                currA = headB
                
            if currB.next:
                currB = currB.next 
            else:
                currB = headA
                
            if currA is currB:
                return currA
                
    def have_intersection(self, headA, headB):
        if not headA or not headB:
            return False
        while headA.next:
            headA = headA.next
        while headB.next:
            headB = headB.next
        return headA is headB
        
                
            
