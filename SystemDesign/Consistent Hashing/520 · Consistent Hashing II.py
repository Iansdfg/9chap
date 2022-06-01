class Solution:
    """
    @param {int} n a positive integer
    @param {int} k a positive integer
    @return {Solution} a Solution object
    """
    @classmethod
    def create(cls, n, k):
        # Write your code here
        solution = cls()
        solution.ids = {}
        solution.machines = {}
        solution.n = n 
        solution.k = k 
        return solution

    """
    @param: machine_id: An integer
    @return: a list of shard ids
    """
    def addMachine(self, machine_id):
        # write your code here
        ids = []
        import random
        for i in range(self.k):
            index = random.randint(0, self.n - 1)
            while index in ids:
                index = random.randint(0, self.n - 1)
            ids.append(index)
            self.ids[index] = True 
        
        ids.sort()
        self.machines[machine_id] = ids 
        return ids

    """
    @param: hashcode: An integer
    @return: A machine id
    """
    def getMachineIdByHashCode(self, hashcode):
        # write your code here
        machine_id = -1 
        distance = self.n + 1 

        for key, val in self.machines.items():
            import bisect
            # use mode so it new ele is largest, inster in the left most place
            index = bisect.bisect_left(val, hashcode) % len(val)
            print(bisect.bisect_left(val, hashcode), len(val), index)#
            d = val[index] - hashcode
            if d < 0:
                d += self.n
            if d < distance:
                distance = d
                machine_id = key 
        return machine_id


