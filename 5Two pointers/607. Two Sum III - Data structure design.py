class TwoSum:
    numbers = []
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        self.numbers.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        num_list = sorted(self.numbers)
        # print(num_list)
        if self.TwoSum_func(value, num_list):
            return True
        return False
        
    def TwoSum_func(self, target, arrary):
        dic = {}
        for pos, number in enumerate(arrary):
            if number not in dic:
                dic[target - number]= pos
            else:
                return True
        return False
        
        
        
        
        
