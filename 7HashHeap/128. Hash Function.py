class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        ans = 0
        for char in key:
            ans = (ans*33+ord(char))%HASH_SIZE

        return ans 
        
