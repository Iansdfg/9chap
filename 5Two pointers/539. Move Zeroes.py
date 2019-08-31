class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        left,right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        # zero_pose = 0
        # non_zero_pose = 0
        # while zero_pose<len(nums)-1:
        #     if nums[zero_pose]!=0:
        #         zero_pose+=1
        #     else:
        #         zero_pose = zero_pose
        #         while nums[non_zero_pose]==0:
        #             non_zero_pose+=1
        #             if non_zero_pose > len(nums)-1:
        #                 return 
        #         nums[zero_pose], nums[non_zero_pose] = nums[non_zero_pose],nums[zero_pose]
        #     zero_pose+=1
        
                
