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
        
        
        
# merge 
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
        
        return self.devide_and_merge(lists, 0, len(lists)-1)
        
        
    def devide_and_merge(self, lists, start, end):
        if start == end:
            return lists[start]
        
        mid = (start + end)//2
        left = self.devide_and_merge(lists, start, mid)
        right = self.devide_and_merge(lists, mid+1, end)
        return self.merge_two_list(left, right)
        
        
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
        
        
        
        


# heap
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

from heapq import heappop, heappush
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        heap = []
        result = []
        
        for index, head in enumerate(lists):
            if not head:
                continue
            heappush(heap, (head.val, index, head))
            
        dummy = ListNode(0)
        tail = dummy
        
        while heap:
            node_val, node_index, node = heappop(heap)
            print(node_val, node_index)
            tail.next = node
            tail = node
            if not node.next:
                continue
            nextt = node.next
            heappush(heap, (nextt.val, node_index  , nextt))
            
        return dummy.next 
        


        


