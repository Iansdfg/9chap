class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left + 1 < right:
            mid = (left + right)//2

            if nums[mid] > nums[left]:
                if nums[left] <= target < nums[mid]:
                    #没有 <= nums[mid] 因为把 == mid 的情况留到了else处理
                    right = mid
                else:
                    left = mid

            elif nums[mid] < nums[left]:
                if  nums[mid] < target < nums[left]: 
                    #没有 <=, 因为是left，包含了right的边界
                    left = mid 
                else:
                    right = mid 


        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right 
        else:
            return -1 

        
