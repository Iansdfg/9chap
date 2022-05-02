class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
             we will sort your return value in output
    """
    def accounts_merge(self, accounts):
        # write your code here

        # init 
        result = []
        self.father = dict()
        self.owner = dict()
        self.mp = dict()
        for account in accounts:
            n = len(account)
            for i in range(1,n):
                # this account's father is itself
                self.father[account[i]] = account[i]
                # the owner of this accound is username 
                self.owner[account[i]] = account[0]
        # union all the emails under the same account
        for account in accounts:
            n = len(account)
            for i in range(2,n):
                # let email 1 be the root of all other email 
                # make b a's father
                self.union(account[i], account[1])
        # build map {key: email father, value: emails}
        for account in accounts:
            n = len(account)
            for i in range(1,n):
                father = self.find(account[i])
                if father not in self.mp:
                    self.mp[father] = []
                self.mp[father].append(account[i])

        for key in self.mp:
            record = []
            record.append(self.owner[key])
            others = self.mp[key]
            others = sorted(list(set(others)))
            record = record + others
            result.append(record)
        return result 

    def union(self, a, b):
        #uniom two element 
        fa, fb = self.find(a), self.find(b)
        if fa != fb:
            self.father[fa] = fb

    def find(self, s):
        #return the father root or a element
        if self.father[s] == s:
            return s 
        self.father[s] = self.find(self.father[s])
        return self.father[s]

            




