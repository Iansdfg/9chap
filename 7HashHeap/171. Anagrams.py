class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        # write your code here
        res = []
        string2freg = {}
        for string in strs:
            sort_srt = ''.join(sorted(str(string)))
            if sort_srt in string2freg:
                string2freg[sort_srt] += 1
            else:
                string2freg[sort_srt] = 1
        for string in strs:
            sort_srt = ''.join(sorted(str(string)))
            if string2freg[sort_srt]>1:
                res.append(string)
        return res


