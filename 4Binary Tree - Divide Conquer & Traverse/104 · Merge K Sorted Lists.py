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
        return self.dfs(lists, 0, len(lists))

    def dfs(self, lists, start, end):
        # return merged two list
        if start == end - 1:
            return lists[start]
        mid = (start + end) // 2 
        left_list = self.dfs(lists, start, mid)
        right_list = self.dfs(lists, mid, end)

        return self.merge2Lists(left_list, right_list)

    def merge2Lists(self, l1, l2):
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
        if l1 or l2:
            tail.next = l1 or l2 

        return dummy.next

        

