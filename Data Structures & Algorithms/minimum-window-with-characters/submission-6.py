class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        min_len = float("inf")
        counts_s, counts_t = defaultdict(int), defaultdict(int)
        shortest = ""

        for char in t:
            counts_t[char] += 1
        
        required = len(counts_t)
        satisfied = 0

        for right, char in enumerate(s):
            counts_s[char] += 1

            if char in counts_t and counts_s[char] == counts_t[char]:
                satisfied += 1

            while satisfied == required and left <= right:
                curr_len = right + 1 - left
                if curr_len < min_len:
                    min_len = curr_len
                    shortest = s[left:right + 1]

                removed = s[left]
                counts_s[removed] -= 1
                if counts_s[removed] < counts_t[removed]:
                    satisfied -= 1

                left += 1
        
        return shortest

                





        






            




