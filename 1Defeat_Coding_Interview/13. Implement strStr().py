class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        if source == target or target ==:
            return 0
        for pos, val in enumerate(source):
            if val == target[0]:
                if target == source[pos:pos + len(target)]:
                    return pos 
        return -1
                        
