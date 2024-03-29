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

        while len(lists) > 1:
            new_list = []
            for i in range(0, len(lists), 2):
                if i+1 < len(lists):
                    new_list.append(self.merge_two(lists[i], lists[i+1]))
                else:
                    new_list.append(lists[i])
            lists = new_list
        return lists[0]
                    
        
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
import heapq
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
        heap = []
        for index, head in enumerate(lists):
            if not head:
                continue
            heapq.heappush(heap, (head.val, head))

        dummy = ListNode(-1)
        tail = dummy
        while heap:
            curr_val, curr_node = heapq.heappop(heap)
            tail.next = curr_node
            tail = curr_node

            next_node = curr_node.next
            if not next_node:
                continue
            heapq.heappush(heap, (next_node.val, next_node))
        
        return dummy.next
            
            
