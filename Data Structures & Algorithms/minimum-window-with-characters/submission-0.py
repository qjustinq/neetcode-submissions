class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #wow this was hard
        if t == "":
            return ""

        window = {}
        count = {}

        res = [-1,-1]
        resLen = float("infinity")
        pointer_left = 0

        for i in t:
            count[i] = 1 + count.get(i,0)

        have = 0
        need = len(count)

        for i in range(len(s)):
            current_character = s[i]
            window[current_character] = 1 + window.get(current_character, 0)
            
            if current_character in count and window[current_character] == count[current_character]:
                have += 1

            while have == need:
                if (i - pointer_left + 1) < resLen:
                    res = [pointer_left, i]
                    resLen = (i - pointer_left + 1)
                window[s[pointer_left]] -= 1
                if s[pointer_left] in count and window[s[pointer_left]] < count[s[pointer_left]]:
                    have -= 1
                pointer_left += 1


        pointer_left , i = res
        return s[pointer_left: i +1] if resLen != float("infinity") else  ""
        

        

        