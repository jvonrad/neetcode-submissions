class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 1
        curr_set = set(s[left:right])
        max_len = len(curr_set)
        
        # "abcbde"
        while right < len(s):
            new_char = s[right]
            if new_char not in curr_set:
                curr_set.add(new_char)
                curr_len = len(curr_set)
                max_len = max(curr_len, max_len)
                right += 1
            else:
                curr_set.remove(s[left])
                left += 1    

        return max_len

                
            



        
        
                


        