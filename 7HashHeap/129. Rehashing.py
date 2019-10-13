"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        new_table = [None]*(len(hashTable)*2)
        for ele in hashTable:
            node = ele
            while node:
                self.add_node(node.val, new_table)
                node = node.next
        return new_table
        
    def add_node(self, old_value, table):
        new_key = old_value % len(table)
        if not table[new_key]:
            table[new_key] = ListNode(old_value)
        else:
            self.add_list(table[new_key], ListNode(old_value))
        
    def add_list(self, head, new_node):
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = new_node
