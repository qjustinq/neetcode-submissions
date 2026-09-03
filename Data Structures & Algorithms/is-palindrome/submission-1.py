class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = "".join(char.lower() for char in s if char.isalnum())
        pointer_1 = 0 
        pointer_2 = len(new_string) -1
        for i in range(len(new_string)):
            if new_string[pointer_1] == new_string[pointer_2]:
                pointer_1 += 1
                pointer_2 -= 1
            else:
                return False

        return True