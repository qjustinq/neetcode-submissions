class Solution:

    def encode(self, strs: List[str]) -> str:
        str_var = ""
        for i in strs:
            str_len = len(i)
            str_var += str(str_len) + "#" + i
        return str_var


    def decode(self, s: str) -> List[str]:
        str_list = []
        i = 0 
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            str_list.append(s[j+1 : j+1 + length])

            i = j + 1 + length
        return str_list