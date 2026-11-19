class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        counts = defaultdict(int)

        # "AAABABB"
        for right, char in enumerate(s):
            counts[char] += 1

            while (right + 1 - left) > max(counts.values()) + k:
                counts[s[left]] -= 1
                left += 1

            max_len = max(max_len, right + 1 - left)

        return max_len

            

            
                




            




        