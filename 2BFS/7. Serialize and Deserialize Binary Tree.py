class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        if org == []: return True 
        if seqs == [] or seqs[0]==[]: return False
        graph = {n:[] for n in org}
        indegree = [0 for n in range(len(org)+1)]
        
        for seq in seqs:
            if seq[0]>len(org): return False 
            for pos in range(len(seq)-1, 0, -1):
                if seq[pos]>len(org): return False 
                if seq[pos-1] in graph[seq[pos]]:
                    continue
                graph[seq[pos-1]].append(seq[pos])
                indegree[seq[pos]]+=1
        
        queue = collections.deque()
        
        for i in range(1,len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        order = []
        while queue:
            if len(queue)>1:
                return False
            curr_node = queue.popleft()
            order.append(curr_node)
            for next_node in graph[curr_node]:
                indegree[next_node]-=1
                if indegree[next_node] == 0:
                    queue.append(next_node)
        return len(order) == len(org) and order == org
  
        
