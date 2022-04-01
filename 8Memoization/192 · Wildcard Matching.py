class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def is_match(self, s, p):
        # write your code here
        return self.is_match_helper(s, 0, p, 0, {})


    def is_match_helper(self, s, i, p, j, memo):
        print(s[i:], p[j:])
        if (i, j) in memo:
            return memo[(i, j)]

        if len(s) == i:
            # s is empty, then p have to be 
            # all * to make it match
            for char in p[j:]:
                if char != '*':
                    return False
            return True

        if len(p) == j: 
            return False 

        if p[j] == "*":
            # if p = *XXX, s= YYYY (*a, a) (*, a)
            # next p,s: XXX, YYYY (a, a)or *XXX, YYY (*, '')
            # either match return True 
            match = self.is_match_helper(s, i + 1, p, j, memo) or self.is_match_helper(s, i, p, j + 1, memo)
        else:
            match = self.is_char_match(s[i], p[j]) and self.is_match_helper(s, i + 1, p, j + 1, memo)

        memo[(i, j)] = match
        return match

    def is_char_match(self, s, p):
        return s==p or p=='?'
