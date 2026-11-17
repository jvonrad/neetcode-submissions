class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        # forward pass (prefix)
        prefix = 1
        # nums =   [2,4,1,3]
        # output = [1,2,8,8]
        for i, num in enumerate(nums):
            output[i] *= prefix
            prefix *= num

        suffix = 1
        # suffix = [,3,3,1]
        # nums =   [2,4,1,3]
        # output = [1,2,24,8]
        for i in range(len(nums)-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output
             


            
        
        return output

        