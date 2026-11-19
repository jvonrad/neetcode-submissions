class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # initialize variables
        left = 0
        min_len = float("inf")
        shortest = ""
        counts_s, counts_t = defaultdict(int), defaultdict(int)

        # count target string frequencies once
        for char in t:
            counts_t[char] += 1
        
        # helpers
        required = len(counts_t)
        satisfied = 0

        for right, char in enumerate(s):
            counts_s[char] += 1
            
            # check if one character required was satisfied
            if char in counts_t and counts_s[char] == counts_t[char]:
                satisfied += 1

            # if all satisfied, try to make smaller
            while required == satisfied and left <= right:
                curr_len = right + 1 - left
                if curr_len < min_len:
                    min_len = curr_len
                    shortest = s[left:right + 1]
                
                # remove left-most char
                removed = s[left]
                counts_s[removed] -= 1
                if removed in counts_t and counts_s[removed] < counts_t[removed]:
                    satisfied -= 1

                # move pointer further 
                left += 1

        return shortest






            




