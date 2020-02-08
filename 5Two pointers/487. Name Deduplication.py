class Solution:
    """
    @param names: a string array
    @return: a string array
    """
    def nameDeduplication(self, names):
        # write your code here
        new_names = []
        for name in names:
            new_names.append(name.lower()) 
        print(new_names)
        
        
        length = len(new_names)
        if length == 0:
            return []
        new_names.sort()
        slow = 0
        for fast in range(1, len(new_names)):
            if new_names[fast] != new_names[slow]:
                slow += 1 
                new_names[slow] = new_names[fast]
        return new_names[:slow+1]
                
            
