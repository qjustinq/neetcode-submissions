class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #We just use a dictonary to count the appearances of the letters
        count_s = {}
        count_t = {}
        for i in s:
            if i not in count_s:
                count_s[i] = 1
            else: 
                count_s[i] += 1

        for i in t:
            if i not in count_t:
                count_t[i] = 1
            else: 
                count_t[i] += 1

        if count_t == count_s:
            return True
        else:
            return False