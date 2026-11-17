class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums) # O(n)
        longest = 0

        for num in unique_nums:
            # identify start candidates
            if num - 1 not in unique_nums:
                length = 1

                # count sequence length
                while num + length in unique_nums:
                    length += 1

                longest = max(length, longest)

        return longest

                
                
                




        
    


            


        