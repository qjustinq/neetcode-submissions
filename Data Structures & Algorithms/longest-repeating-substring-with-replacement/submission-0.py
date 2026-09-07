class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        pointer_left = 0 
        max_freq = 0

        for i in range(len(s)):
            counter[s[i]] = 1 + counter.get(s[i] ,0)
            if  i -pointer_left + 1 - max(counter.values()) > k:
                counter[s[pointer_left]] -= 1
                pointer_left += 1

            max_freq = max(max_freq, i - pointer_left + 1)

        return max_freq
        
            