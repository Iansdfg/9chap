class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def str_str(self, source, target):
        # Write your code here
        # if target not in source:
        #     return -1

        for i in range(len(source)-len(target)+1):
            if source[i:i+len(target)] == target:
                return i
        return -1
