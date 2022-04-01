class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def is_match(self, s, p):
        # write your code here

        return self.is_match_helper(s, 0, p, 0, dict())

    def is_match_helper(self, s, i, p, j, memo):
        #memo store if s[i:] and p[j:] can match 
        if (i,j) in memo:
            return memo[(i,j)]

        if len(s) == i:
            return self.is_empty(p[j:])

        if len(p) == j:
            return False 

        if j + 1 < len(p) and p[j + 1] == '*':
            is_curr_char_match = self.is_match_char(s[i], p[j]) 
            next_s_match = self.is_match_helper(s, i + 1, p, j, memo)
            next_p_match = self.is_match_helper(s, i, p, j + 2, memo)
            
            match = is_curr_char_match and next_s_match or next_p_match
            # match2 = next_s_match or next_p_match
            # case s == "aab" p == "c*a*b" for next_p_match need no is_curr_char_match
            # case s == "ab" p == "b*" for next_s_match need is_curr_char_match
            # print(s, p, i, j, s[i:],p[j:], match, is_curr_char_match, next_s_match, next_p_match)

        else:
            match = self.is_match_char(s[i], p[j]) and self.is_match_helper(s, i + 1, p, j + 1, memo)

        memo[(i,j)] = match
        return match

    def is_match_char(self, s, p):
        return s==p or p=='.'

    def is_empty(self, p):
        #if len of p is odd, cannot be empty
        if len(p) % 2 == 1:
            return False 
        else:
        # if len of p is even, only folloing return True:
        # X*...X*
            for i in range(len(p) // 2):
                if p[i*2+1] != '*':
                    return False 
        return True 
