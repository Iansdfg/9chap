class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def is_match(self, s, p):
        # write your code here
        return self.is_match_helper(s, 0, p, 0, {})

    def is_match_char(self, s, p):
        return s == p or p == '?'


    def is_match_helper(self, s, i, p, j, memo):
        #meno store if s[i:] match p[j:]
        if (i,j) in memo:
            return memo[(i,j)]

        #if s is empty, all char in p need to be *
        if len(s) == i:
            for char in p[j:]: 
                if char != '*':
                    return False 
            return True 

        if len(p) == j:
            return False 

        if p[j] != '*':
            is_char_match = self.is_match_char(s[i], p[j])
            is_rest_match = self.is_match_helper(s, i + 1, p, j + 1, memo)
            match = is_char_match and is_rest_match

        else:
            match = self.is_match_helper(s, i, p, j + 1, memo) or self.is_match_helper(s, i + 1, p, j, memo)

        memo[(i,j)] = match

        return match

        
