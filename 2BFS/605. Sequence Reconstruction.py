class Node:
    def __init__(self, val):
        self.val = val
        self.neighbers = []

from collections import deque
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequence_reconstruction(self, org, seqs):
        # write your code here
        if not seqs or not seqs[0]:
            return org  == []
        node2neighbers = {x:[] for x in org}
        node2indegree = {x:0 for x in org}
        for seq in seqs:
            for i in range(len(seq)):
                if seq[i] > len(org):
                    return False
                if i == 0:
                    continue
                node2indegree[seq[i]] += 1 
                node2neighbers[seq[i - 1]].append(seq[i])

        queue = deque([])
        for key in node2indegree:
            if node2indegree[key] == 0:
                queue.append(key)

        topological_order = []
        
        while queue:
            if len(queue) > 1:
                return False
            curr = queue.popleft()
            topological_order.append(curr)
            for next_node in node2neighbers[curr]:
                node2indegree[next_node] -= 1
                if node2indegree[next_node] == 0:
                    queue.append(next_node)

        return topological_order == org







