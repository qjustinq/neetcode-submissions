class Solution:
    def isValid(self, s: str) -> bool:
        #return back to study
        map = {")" : "(", "]" : "[" , "}" : "{"}
        stack = []

        for i in s:
            if i not in map:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    pop = stack.pop()
                    if pop != map[i]:
                        return False

        return not stack