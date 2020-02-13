from random import randint
class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.id_to_idx = {}

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        # write your code here
        if server_id in self.id_to_idx:
            return
        self.stack.append(server_id)
        self.id_to_idx[server_id] = len(self.stack) - 1 
        

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        # write your code here
        if server_id not in self.id_to_idx:
            return
        
        pos = self.id_to_idx[server_id]
        del self.id_to_idx[server_id]
        
        last_id = self.stack[-1]
        
        self.id_to_idx[last_id] = pos
        self.stack[pos] = last_id
        
        self.stack.pop()
        

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        # write your code here
        ran_pos = randint(0, len(self.stack) - 1)
        return self.stack[ran_pos]
