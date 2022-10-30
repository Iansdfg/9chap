class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        dic = {}
        
        for pos, number in enumerate(numbers):
            if number not in dic:
                dic[target - number]= pos
            else:
                return [dic[number], pos]
            
        return [-1, -1]

    
    
    
    
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        dic = {}
        for pos, number in enumerate(numbers):
            if number not in dic:
                dic[number] = [pos]
            else:
                dic[number].append(pos)
            
            val = target - number
        
            if val in dic and val != number:
                index = dic[val][0]
                return [index, pos]
                
            if val in dic and val == number and len(dic[number]) > 1:
                index_list = dic[number]
                return [min(index_list), max(index_list)]
