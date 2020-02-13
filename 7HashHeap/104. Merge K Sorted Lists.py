"Two-Two Merger"
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if not lists: return lists
        
        while len(lists) > 1:
            next_lists = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    new_list = self.merge_two_list(lists[i], lists[i+1])
                else:
                    new_list = lists[i]
                next_lists.append(new_list)
            lists = next_lists
        
        return lists[0]
        
        
    def merge_two_list(self, l1, l2):
        dummy = tail = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        return dummy.next
        
"D-C Merger"  
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if len(lists) == 1:
            return lists[0]
            
        if len(lists) == 2:
            return self.merge_two(lists[0], lists[-1])
    
        mid = (len(lists))//2
        left_list = self.mergeKLists(lists[:mid])
        right_list = self.mergeKLists(lists[mid:])
        
        
        return self.merge_two(left_list, right_list)
        
        
    def merge_two(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy 
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
            
        return dummy.next
          

# heap
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

from heapq import heappop, heappush, heapify
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        heap = []
        for index, head in enumerate(lists):
            if not head:
                continue
            heappush(heap, (head.val, index, head))
            
        dummy = ListNode(0)
        tail = dummy
        while heap:
            curr_val, curr_idx, curr = heappop(heap)
            tail.next = curr
            tail = curr
            
            nextt = curr.next
            if not nextt:
                continue
            heappush(heap, (nextt.val, curr_idx, nextt))
            
        return  dummy.next
            
