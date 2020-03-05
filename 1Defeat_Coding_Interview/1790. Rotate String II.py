class Solution:
    """
    @param str: An array of char
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """
    def RotateString2(self, str, left, right):
        # write your code here
        offset = (left - right) % len(str)
        mainStr = str[offset:]
        subStr = str[:offset]
        return mainStr + subStr
    
class Solution:
    """
    @param str: An array of char
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """
    def RotateString2(self, str, left, right):
        # write your code here
        lenth = len(str)
        left = left % lenth
        right = right % lenth
        move_left = left - right
        return str[move_left:] + str[:move_left]
