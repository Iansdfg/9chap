class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        # write your code here
        anagram_to_list = dict()
        for string in strs:
            anagram = ''.join(sorted(string))
            if anagram in anagram_to_list:
                anagram_to_list[anagram].append(string)
            else:
                anagram_to_list[anagram] = [string]

        results = []
        for key in anagram_to_list:
            if len(anagram_to_list[key]) >= 2:
                results += anagram_to_list[key]
                
        return results
