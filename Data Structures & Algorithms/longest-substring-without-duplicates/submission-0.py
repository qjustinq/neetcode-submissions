class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #visit back to study more
        string_set = set()
        pointer_left = 0
        answer = 0 

        for i in range(len(s)):
            while s[i] in string_set:
                string_set.remove(s[pointer_left])
                pointer_left += 1
            string_set.add(s[i])
            answer = max(answer, i - pointer_left + 1)

        return answer 



            