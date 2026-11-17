class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_s = ""
        for s in strs:
            encoded_s += str(len(s)) + "#" +  s

        return encoded_s

    # "5#Hello5#World"
    def decode(self, s: str) -> List[str]:
        words = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            # read word length (can be multiple digits)
            curr_len = int(s[i:j])

            # based on word length extract word
            start, end = j+1, j+1+curr_len
            curr_word = s[start:end] # (end is excluded)

            # add word to words
            words.append(curr_word)

            # continue at next word
            i = end 

        return words


            


            
            
