class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        min_len = float("inf") 
        shortest = ""
        counts_s = defaultdict(int)
        counts_t = defaultdict(int)

        for char in t:
            counts_t[char] += 1

        required = len(counts_t)
        satisfied = 0

        # "OUZODYXAZV"
        for right, char in enumerate(s):
            counts_s[char] += 1

            if char in counts_t and counts_s[char] == counts_t[char]:
                satisfied += 1

            while required == satisfied and left <= right:
                curr_len = right + 1 - left

                if curr_len < min_len:
                    shortest = s[left:right + 1]
                    min_len = curr_len

                counts_s[s[left]] -= 1
                
                if s[left] in counts_t and counts_s[s[left]] < counts_t[s[left]]:
                    satisfied -= 1

                left += 1    

                

        return shortest


            




