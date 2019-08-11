class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        if target == '': return 0
        target_lenth = len(target)
        target_source = len(source)
        for i in range(target_source-target_lenth+1):
            if source[i:i+target_lenth] == target:
                return i
        return -1
