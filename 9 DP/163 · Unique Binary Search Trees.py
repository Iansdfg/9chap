class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def num_trees(self, n):
        # write your code here
        nodes_trees = {
            0:1,
            1:1,
            2:2,
        }
        return self.helper(n, nodes_trees)
        
    def helper(self, n, nodes_trees):
        if n in nodes_trees:
            return nodes_trees[n]

        res = 0
        for i in range(n):
            res += self.helper(i, nodes_trees) * self.helper(n - i - 1, nodes_trees)
        nodes_trees[n] = res 
        return res 
