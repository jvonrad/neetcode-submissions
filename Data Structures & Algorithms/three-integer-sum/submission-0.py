class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        # input: [-1,0,1,2,-1,-4]
        # sorted:[-4,-1,-1,-1, 0,1,2]
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = num + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    output.append([num, nums[left], nums[right]])
                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return output




                    


                



            


