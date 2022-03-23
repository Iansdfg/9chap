class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def first_unique_number(self, nums, number):
        # Write your code here
        if number not in nums:
            return -1
        num_to_freq = dict()
        for num in nums:
            if num == number:
                num_to_freq[num] = 1
                break 
            if num in num_to_freq:
                num_to_freq[num] += 1 
            else:
                num_to_freq[num] = 1

        for num in nums:
            if num_to_freq[num] == 1:
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
            
