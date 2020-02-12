class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        # Write your code here
        if len(nums)==0:
            return -1 
        if number not in nums:
            return -1 
            
        num_to_times = dict()
        for num in nums:
            if num in num_to_times:
                num_to_times[num] += 1 
            else:
                num_to_times[num] = 1 
            if num == number:
                break
        
        for num in nums:
            if num in num_to_times and num_to_times[num] == 1 :
                return num
        return -1 
                
                
        
        
        # if not nums:
        #     return -1
        # if number not in nums:
        #     return -1
        
            
        # visited = []
        # results = []
        # for num in nums:
        #     if num == number:
        #         results.append(num)
        #         break
        #     if num in results:
        #         visited.append(num)
        #         results.remove(num)
        #     else:
        #         results.append(num)
                
        # print(results, visited)
        # for result in results:
        #     if result in visited:
        #         continue 
        #     return result
            
        # return -1 
            
